import _sqlite3

conn = _sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEES(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL NOT NULL
);''')
print("Table created successfully")
conn.close()
