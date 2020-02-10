# sqlite3
import sqlite3
import datetime

def connect():
    dbName = 'login.db'
    conn = sqlite3.connect(f'{dbName}')

    cursor = conn.cursor()
    return conn, cursor


def createTable():
    conn, cursor = connect()
    tbLogin = 'CREATE TABLE tbLogin (id int, loginName text, loginpass text, date datetime)'
    cursor.execute(f'{tbLogin}')
    conn.commit()

def insertToTable():
    conn, cursor = connect()
    today = datetime.date.today
    tbInsert = f"INSERT INTO tbLogin values ('rowid', 'viperdavid', 'test', '{today})"
    cursor.execute(f'{tbInsert}')
    conn.commit()

def select():
    conn, cursor = connect()
    tbSelect = "Select * from tbLogin;"
    s = cursor.execute(f'{tbSelect}')
    return s

    conn.close()


def main():
    #createTable()
    insertToTable()
    conn, cursor = connect()
    #c = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for i in select():
        print(i)


main()