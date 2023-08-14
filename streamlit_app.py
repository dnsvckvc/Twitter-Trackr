import streamlit as st
import sqlite3
import pandas as pd
import time
import os
import tweepy
from database.twitter_database import get_liked_tweets_by_user_id, get_num_of_rows
from twitter_api import read_csv_file, get_user_ids

st.set_page_config(layout="wide")
st.header("Twitter Trackr")


CSV_FILE_PATH = 'accounts.csv'


def show_data():
    usernames = read_csv_file('accounts.csv')
    user_ids = get_user_ids(CSV_FILE_PATH, tweepy.Client(bearer_token=os.environ['BEARER_TOKEN']))
    conn = sqlite3.connect('database/twitter_database.db')
    cursor = conn.cursor()

    for index, user_id in enumerate(user_ids):
        st.subheader(f"Liked Tweets for {usernames[index]}")

        bottom_menu = st.columns((4, 1, 1))
        with bottom_menu[2]:
            page_size = st.selectbox("Page Size", options=[10, 25, 50], index=0, key=f"page_size_{user_id}")

        total_pages = (get_num_of_rows(cursor, user_id) + page_size - 1) // page_size # TODO CHANGE 11 WITH PROPER VALUE

        with bottom_menu[1]:
            current_page = st.number_input("Page", min_value=1, max_value=total_pages, step=1, key=f"current_page_{user_id}")

        with bottom_menu[0]:
            st.markdown(f"Page **{current_page}** of **{total_pages}**")

        liked_tweets = get_liked_tweets_by_user_id(cursor, user_id, page_size, current_page)
        df = pd.DataFrame(liked_tweets, columns=["Tweet ID", "Tweet Text", "Liked at"])

        df["Liked at"] = pd.to_datetime(df["Liked at"]).dt.strftime('%Y-%m-%d')  # Format the date

        df["URL"] = [f"https://twitter.com/twitter_user/status/{tweet_id}" for tweet_id in df["Tweet ID"]]

        df.index = df.index + 1 + ((current_page - 1) * page_size)

        st.dataframe(data=df, use_container_width=True)
    conn.close()


if __name__ == "__main__":
    while(True):
        show_data()
        time.sleep(24 * 60 * 60)    # 1 day = 24*60*60 = 86400s
        st.experimental_rerun()