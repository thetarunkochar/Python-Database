import sqlite3

def create():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists store(item TEXT,quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

insert('Pens', 10, 20)

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows

data = view()
for d in data:
    print(d)

# test 
