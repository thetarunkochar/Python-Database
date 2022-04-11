import psycopg2


def create():
    conn = psycopg2.connect(
        "dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students(id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, grade INTEGER, total_score INTEGER, gender TEXT, result TEXT, age INTEGER) ")
    conn.commit()
    conn.close()

create()

def insert(first_name, last_name, grade, total_score, gender, result, age):
    conn = psycopg2.connect(
        "dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('INSERT INTO students (first_name, last_name, grade, total_score, gender, result, age) VALUES(%s, %s, %s,%s, %s, %s, %s)',(first_name, last_name, grade, total_score, gender, result, age))
    conn.commit()
    conn.close()

# insert('Virat', 'Kohli', 6, 55, 'M', 'PASS', 34)
# insert('Tarun', 'Kochar', 8, 30, 'M', 'Fail', 12)
# insert('Alexa', 'Amazon', 1, 99, 'F', 'PASS', 5)
# insert('Jolly', 'Singh', 10, 45, 'F', 'HOLD', 12)
# insert('Sara', 'Gill', 6, 35, 'F', 'FAIL', 25)
# insert('Shubhman', 'Tendulkar', 6, 99, 'M', 'PASS', 26)
# insert('Jay', 'Kohli', 10, 85, 'M', 'PASS', 34)

def view():
    conn = psycopg2.connect(
        "dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('SELECT * FROM students')
    rows = cur.fetchall()          
    conn.close()
    return rows

def view_gradewise(grade):
    conn = psycopg2.connect(
        "dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('SELECT * FROM students where grade = %s', (grade,))
    #cur.execute('SELECT * FROM students')
    rows = cur.fetchall()          
    conn.close()
    return rows

def view_lastnamewise():
    conn = psycopg2.connect(
        "dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * from students where last_name like 'G%'")
    #cur.execute('SELECT * FROM students')
    rows = cur.fetchall()          
    conn.close()
    return rows

def update_grade(grade_i, grade_f, firstname):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE students SET grade =%s WHERE first_name LIKE %s and grade = %s', (grade_f, firstname, grade_i))
    conn.commit()
    conn.close()

def delete_agewise(age):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('DELETE FROM students WHERE age = %s', (age,))
    conn.commit()
    conn.close()

def update_result(thresold):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE students SET result = "FAIL" WHERE total_score < %s', (thresold,))
    conn.commit()
    conn.close()

def update_result_age(age):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE students SET result = "HOLD" WHERE age < %s', (age,))
    conn.commit()
    conn.close()

def delete_gradewise(grade):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('DELETE FROM students WHERE grade = %s', (grade,))
    conn.commit()
    conn.close()


def update_gender(result):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE students SET gender = "M" WHERE result LIKE %s', (result,))
    conn.commit()
    conn.close()

def update_lastname(firstname, lastname):
    conn = psycopg2.connect("dbname='assignment_students' user = 'tarun' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE students SET last_name = %s WHERE first_name LIKE %s', (lastname, firstname))
    conn.commit()
    conn.close()

# update_grade(6, 10, "Virat")
# delete_agewise(26)
update_lastname('Sara', 'Gilll')
data = view()
for d in data:
    print(d)

