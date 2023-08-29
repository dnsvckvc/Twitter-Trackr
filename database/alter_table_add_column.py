# import the module sqlite3
import sqlite3

# Make a connection to the SQLite DB
dbCon = sqlite3.connect("twitter_database.db")

# Obtain a Cursor object to execute SQL statements
cur   = dbCon.cursor()
 
# Add a new column to student table
addColumns = "ALTER TABLE liked_tweets \
    ADD COLUMN Username VARCHAR(255), \
    ADD COLUMN Author_id INTEGER"
    
cur.execute(addColumns)

dbCon.close()