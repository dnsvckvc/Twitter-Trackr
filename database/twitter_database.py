import sqlite3

# create the 'liked_tweets' table
def create_liked_tweets_table(cursor):
    print("Creating 'liked_tweets' table in database...")
    cursor.execute('''
        CREATE TABLE liked_tweets (
            user_id INTEGER,
            tweet_id INTEGER,
            text TEXT,
            PRIMARY KEY (user_id, tweet_id)
        )
    ''')
    print("Table 'liked_tweets' is created in database...")


def insert_liked_tweets(cursor, user_id, liked_tweets):
    print(f'Saving liked tweets in database for person with id {user_id}...')
    for tweet in liked_tweets:
        cursor.execute("INSERT OR IGNORE INTO liked_tweets(user_id, tweet_id, text) VALUES (?, ?, ?)", (user_id, tweet.id, tweet.text))
    print(f'Liked tweets are inserted in database for person with id {user_id}...')


def update_database(curos, user_id, new_liked_tweets):
    pass
