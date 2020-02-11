# sqlite3
import sqlite3
from datetime import datetime

def connect():
    dbName = 'login.db'
    conn = sqlite3.connect(f'{dbName}')

    cursor = conn.cursor()
    return conn, cursor


def createTable():
    conn, cursor = connect()
    tbLogin = 'CREATE TABLE if not exists tbLogin (id INTEGER PRIMARY KEY AUTOINCREMENT, loginName TEXT NOT NULL UNIQUE, loginpass TEXT NOT NULL, date datetime)'
    cursor.execute(f'{tbLogin};')
    conn.commit()

def insertToTable():
    conn, cursor = connect()
    today = datetime.now()
    tbInsert = f"INSERT INTO tbLogin values ('viperdavid2', 'test', '{today}')"
    cursor.execute(f'{tbInsert};')
    conn.commit()

def select():
    conn, cursor = connect()
    tbSelect = "Select * from tbLogin;"
    s = cursor.execute(f'{tbSelect};')
    return s

    conn.close()


def main():
    createTable()
    insertToTable()
    conn, cursor = connect()
    #c = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for i in select():
        print(i)


main()
