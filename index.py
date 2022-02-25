#!/usr/bin/python3

import pymysql

# print necessary headers

print("Content-Type: text/html")
print()

conn=pymysql.connect(
    db='testdb',
    user='root',
    passwd='password',
    host='localhost'
)

c = conn.cursor()

c.execute("Select * from test")

for i in c:
    print(i)