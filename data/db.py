import sqlite3

def connect_to_db():
    return sqlite3.connect("articles.db")

