import sqlite3
import re

# TODO Fix import paths: possibly cretate paths.py
def connect_to_db():
    return sqlite3.connect("data/articles.db")

