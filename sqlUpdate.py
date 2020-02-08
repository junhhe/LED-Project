
import pymysql
 #Open database connection

db = pymysql.connect(host="localhost", user="root", passwd="password", db="school")
#prep a cursor object using cursor() method; cursor is like a navigation method
db.autocommit(True)
cursor = db.cursor(pymysql.cursors.DictCursor)


sql = "UPDATE students SET age=16 WHERE name='jun'"
cursor.execute(sql)

cursor.close()
db.close()
