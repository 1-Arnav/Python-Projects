import sqlite3
from sqlite3.dbapi2 import connect

def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn = sqlite3.connect("book.db")
    sql = 'DELETE FROM book WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit
    conn.close()


connect()
#insert("The Sun","John Smith",1918,913123132)
delete(2)
#update(1,"The moon","John Smooth",1917,99999)
print(view())
#print(search(author="John Smooth"))