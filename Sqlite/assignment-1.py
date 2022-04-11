import sqlite3

def create():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    #cur.execute('DROP TABLE customers')
    cur.execute("CREATE TABLE if not exists customers(firstname TEXT, lastname TEXT, age INTEGER, gender TEXT)")
    conn.commit()
    conn.close()

def insert(firstname, lastname, age, gender):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO customers VALUES(?,?,?,?)", (firstname, lastname, age, gender))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('SELECT rowid,* FROM customers')
    rows = cur.fetchall()      
    conn.close()
    return rows

create()
# insert('Tarun', 'Kochar', 22, 'M')
# insert('Virat', 'Kohli', 34, 'M')
# insert('Sachin', 'Tendulkar', 45, 'M')
# insert('Alexandar', 'Jess', 17, 'F')
# insert('Ricky', 'Poiting', 22, 'M')


# First name starts with A
def A():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM customers WHERE firstname LIKE 'A%'")
    rows = cur.fetchall()      
    conn.close()
    return rows

# 2 select all with age > 50
def above50():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM customers WHERE age>50")
    rows = cur.fetchall()      
    conn.close()
    return rows

# 3 users with row id
def withrowid():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM customers")
    rows = cur.fetchall()      
    conn.close()
    return rows

# 4 users with id 4
def withid(id):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM customers WHERE rowid=?", (id,))
    rows = cur.fetchall()      
    conn.close()
    return rows

# 5 updatelastname
def update(id, lastname):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('UPDATE customers SET lastname=? WHERE rowid=?', (lastname, id))
    conn.commit()
    conn.close()

#update(5, 'Pointing')

# 6 delete lastname
def delete(lastname):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM store where lastname=?', (lastname,))
    conn.commit()
    conn.close()

#7 update all genders
def updategender():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE customers SET gender='OTHERS'")
    #cur.execute("UPDATE customers SET gender='F' WHERE gender='M'")
    conn.commit()
    conn.close()

# 8 update gender to female if age below 20
def updategenderbelow20():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE customers SET gender='F' WHERE age<20")
    conn.commit()
    conn.close()


data = withid(5)
for d in data:
    print(d)
