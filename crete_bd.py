from sqlite3 import connect

con = connect('data.db')
cursor = con.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Users (
               id INTEGER UNIQUE,
               username TEXT NOT NULL,
               uid TEXT,
               money INTEGER DEFAULT00,
               tournaments TEXT DEFAULT "{}"
               )
               ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Tournaments (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               description TEXT,
               admin INTEGER,
               count TEXT,
               price INTEGER,
               photo TEXT,
               people TEXT,
               verified INTEGER)
               ''')
con.commit()
con.close()
