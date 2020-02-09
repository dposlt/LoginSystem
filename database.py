# sqlite3
import sqlite3
import datetime

def conn():
    dbName = 'login.db'
    conn = sqlite3.connect(f'{dbName}')

    cursor = conn.cursor()
    return conn, cursor

def createTable(conn, cursor):
    conn, cursor = conn()
    tbLogin = 'CREATE TABLE tbLogin (id int, loginName text, loginpass text, date datetime)'
    cursor.execute(f'{tbLogin}')
    conn.commit()

def insertToTable():
    today = datetime.date.today
    tbInsert = f"INSERT INTO tbLogin values ('rowid', 'viperdavid', 'test', '{today})"
    cursor.execute(f'{tbInsert}')
    conn.commit()

def select():
    tbSelect = "Select * from tbLogin"
    s = cursor.execute(f'{tbSelect}')
    return s

    conn.close()



conn()