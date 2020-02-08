import MySQLdb
 
db = MySQLdb.connect("192.168.0.131","junhhe20","he","junhhe20")
# create cursor 
cursor = db.cursor(MySQLdb.cursors.DictCursor)
db.autocommit(True)
# create table as per requirement
name = 'stephen'
age = 7
gradeLevel = 11
sql = "INSERT INTO students (name,age,gradeLevel) VALUES('stephen',7,11)"
sql2 = "SELECT * from students"
cursor.execute(sql)
cursor.execute(sql2)
# a cursor is predefined clas that can work with mysql

rows = cursor.fetchall()
for row in rows:
	print("name:" + row['name']+"" +" age:" + str(row['age']) + " " + " gradeLevel" + str(row['gradeLevel']))
cursor.close()
db.close()
