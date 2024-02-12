import _sqlite3
conn = _sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'Faith Karimi',23,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'Bob Kuria',32,1500000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'Jane Muthoni',27,45000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'Mary Anne',38,280000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'Paul Kamau',45,500000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()
