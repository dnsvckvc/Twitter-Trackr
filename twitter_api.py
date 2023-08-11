import os, tweepy, csv, sqlite3, time
from database.twitter_database import insert_liked_tweets, create_liked_tweets_table

BEARER_TOKEN = os.environ['BEARER_TOKEN']
CSV_FILE_PATH = 'accounts.csv'

def create_client():
    return tweepy.Client(bearer_token=BEARER_TOKEN)


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
    print("Users ids are loaded depending on username from csv file...")
    return user_ids


def get_liked_tweets(client, id, token=None):
    return client.get_liked_tweets(id, pagination_token=token)


def initial_load(client, account_ids, cursor):
    for id in account_ids: 
        liked_tweets = get_liked_tweets(client, id)
        insert_liked_tweets(cursor, id, liked_tweets.data)


def close_conn(conn):
    conn.commit()
    conn.close()


def daily_update():
    print("Performin daily update...")
    # update_database()
    print("Daily update complete")


if __name__ == "__main__":
    client = create_client()
    account_ids = get_user_ids(CSV_FILE_PATH, client)
    
    if not os.path.exists('database/twitter_database.db'):
        conn = sqlite3.connect('database/twitter_database.db')
        cursor = conn.cursor()
        create_liked_tweets_table(cursor)
        initial_load(client, account_ids, cursor)
        close_conn(conn)
    else:
        print("Ne radi se dnevni update")
    
    while True:
        daily_update()
        time.sleep(86400) # 1 day = 24*60*60 = 86400


