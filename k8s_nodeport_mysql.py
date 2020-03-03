import mysql.connector


mydb = mysql.connector.connect(
  host="10.75.58.92",
  port='30001',
  user="admin",
  passwd="xxxx",
  database='admin'
)

mycursor = mydb.cursor()

mycursor.execute("select * from table01")
'''
for x in mycursor:
  print(x)

id = 5
serial = 5
name = 'BBB'
title = 'se'
years = 23

sql = 'INSERT INTO table01 (id, serial,name,title,years) VALUES ({},{},"{}","{}",{})'.format(id,serial,name,title,years)
'''

'''
try:
  mycursor.execute(sql)
except mysql.connector.errors.IntegrityError as E:
  print(E)

mydb.commit()
'''

myresult = mycursor.fetchall()

for i in myresult:
  print(i)

count = 0
while True:

  mycursor = mydb.cursor()

  mycursor.execute("select * from table01")
  myresult = mycursor.fetchall()

  for i in myresult:
    print(i)
  count +=1