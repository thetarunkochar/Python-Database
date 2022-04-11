import psycopg2


def create():
    conn = psycopg2.connect(
        "dbname='python_test' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER) ")
    conn.commit()
    conn.close()

create()

def insert(first_name, last_name, age):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('INSERT INTO users (first_name, last_name, age) VALUES(%s, %s, %s)',(first_name, last_name, age))
    conn.commit()
    conn.close()

# insert('Virat', 'Kohli', 34)
# insert('Sachin', 'Tendulkar', 44)


def view(firstname):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    # cur.execute('SELECT * FROM users where first_name = %s', (firstname,))
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()          
    conn.close()
    return rows

def delete(id):
    conn = psycopg2.connect("dbname='python_test' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    conn.close()

def update(age, firstname):
    conn = psycopg2.connect("dbname='python_test' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE users SET age =%s WHERE first_name LIKE %s', (age, firstname))
    conn.commit()
    conn.close()


# delete(3)
update(12, 'Virat')

data = view()
for d in data:
    print(d)



