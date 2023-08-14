import os
import tweepy
import csv
import sqlite3
import time
import datetime
from database.twitter_database import insert_liked_tweets, create_liked_tweets_table, update_database
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

BEARER_TOKEN = os.environ['BEARER_TOKEN']
CSV_FILE_PATH = 'accounts.csv'              # Path to the CSV file containing the account usernames
DAYS_TO_KEEP = 30                           # The number of days to keep liked tweets data


def read_csv_file(file_path):
    account_names = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            account_names.append(row[0])
    return account_names


def get_user_ids(file_path, client):
    user_ids=[]
    account_names = read_csv_file(file_path)
    for account_name in account_names:
        username = account_name.split("@")[1]
        user_ids.append(client.get_user(username=username).data.id)
    logging.info("Users ids are loaded depending on username from csv file...")
    return user_ids


def get_liked_tweets(client, id, token=None):
    return client.get_liked_tweets(id, pagination_token=token)


def initial_load(client, account_ids):
    logging.info("Performing initial load...")
    conn = sqlite3.connect('database/twitter_database.db')
    cursor = conn.cursor()
    create_liked_tweets_table(cursor)
    for id in account_ids: 
        liked_tweets = get_liked_tweets(client, id)
        insert_liked_tweets(cursor, id, liked_tweets.data)
    close_conn(conn)
    logging.info("Initial load completed...")


def close_conn(conn):
    conn.commit()
    conn.close()


def delete_older_data(cursor, days_to_keep):
    # Calculate the threshold timestamp for records to be kept (e.g., 30 days ago)
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days_to_keep)
    # Delete records older than the threshold
    cursor.execute("DELETE FROM liked_tweets WHERE inserted_at < ?", (cutoff_date,))


def daily_update(client, account_ids, days_to_keep):
    logging.info(f"Performing daily update for {datetime.datetime.now().strftime('%Y-%m-%d')}...")
    conn = sqlite3.connect('database/twitter_database.db')
    cursor = conn.cursor()

    for user_id in account_ids:
        new_liked_tweets = get_liked_tweets(client, user_id)
        update_database(cursor, user_id, new_liked_tweets.data)

    delete_older_data(cursor, days_to_keep)
    close_conn(conn)
    logging.info("Daily update completed...")


if __name__ == "__main__":
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    account_ids = get_user_ids(CSV_FILE_PATH, client)
    
    while True:
        if not os.path.exists('database/twitter_database.db'):
            initial_load(client, account_ids)
        else:
            daily_update(client, account_ids, DAYS_TO_KEEP)
        time.sleep(86400)   # 1 day = 24*60*60 = 86400s


