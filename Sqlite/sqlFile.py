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

# insert('pens', 10, 20)

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('SELECT rowid,* FROM store ORDER BY item DESC')
    # cur.execute("SELECT rowid,* FROM store WHERE item LIKE 'p%'"    rows = cur.fetchall()          

    rows = cur.fetchall()          
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM store where rowid=?', (id,))
    conn.commit()
    conn.close()

# delete(4)

def update(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))
    conn.commit()
    conn.close()

def update(item, id):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET item=? WHERE rowid=?', (item, id))
def dropTable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE store')
    conn.commit()
    conn.close()
    conn.commit()
    conn.close()
# # update('pens', 100, 76.95)
#update('bookssss', 2)
dropTable()

#update('bookssss', 2)dropTable()


data = view()
for d in data:
    print(d)
