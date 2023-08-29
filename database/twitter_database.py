import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)


def create_liked_tweets_table(cursor):
    logging.info("Creating 'liked_tweets' table in database...")
    cursor.execute('''
        CREATE TABLE liked_tweets (
            user_id VARCHAR(255),
            tweet_id VARCHAR(255),
            text TEXT,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            author_id VARCHAR(255),
            username VARCHAR(255),
            PRIMARY KEY (user_id, tweet_id)
        )
    ''')
    logging.info("Table 'liked_tweets' is created in database...")


def insert_liked_tweets(cursor, user_id, liked_tweets):
    logging.info(f'Saving liked tweets in database for person with id {user_id}...')
    for tweet in liked_tweets:
        cursor.execute("INSERT OR REPLACE INTO liked_tweets(user_id, tweet_id, text, author_id, username) VALUES (?, ?, ?, ?, ?)", (user_id, tweet.id, tweet.text, tweet.author_id, ""))
    logging.info(f'Liked tweets are inserted in database for person with id {user_id}...')


def update_database(cursor, user_id, new_liked_tweets):
    liked_tweets_to_insert = []
    for liked_tweet in new_liked_tweets:
        logging.info(f"Tweet object: {liked_tweet}")
        cursor.execute("INSERT OR REPLACE INTO liked_tweets (user_id, tweet_id, text, author_id, username) VALUES (?, ?, ?, ?, ?)", (user_id, liked_tweet.id, liked_tweet.text, liked_tweet.author_id, ""))
        if cursor.rowcount > 0:
                liked_tweets_to_insert.append(liked_tweet)


def get_liked_tweets_by_user_id(cursor, user_id, page_size, current_page):
    offset = (current_page - 1) * page_size
    query = f'''
        SELECT tweet_id, text, inserted_at, author_id, username
        FROM liked_tweets
        WHERE user_id = ? 
        ORDER BY inserted_at DESC
        LIMIT ? OFFSET ?
    '''
    cursor.execute(query, (user_id, page_size, offset))
    liked_tweets = cursor.fetchall()
    return liked_tweets


def get_num_of_rows(cursor, user_id):
    cursor.execute(f"SELECT COUNT(*) FROM liked_tweets WHERE user_id=?", (user_id,))
    count = cursor.fetchone()[0]
    return count
    