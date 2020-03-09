import matplotlib.pyplot as plt  
import pymysql 

#creating array for temperature, humidity, time 
temp = []
hum = []
tim = []

db = pymysql.connect(host="192.168.0.205", user="humid", passwd="password", db="sensor")
# create cursor 
cursor = db.cursor(pymysql.cursors.DictCursor)
db.autocommit(True)

#select all from weather by time in descending order limiting the data to 5 
sql = "SELECT * from weather ORDER BY time DESC LIMIT 5"

#execute the sql statement
cursor.execute(sql)

# a cursor is predefined clas that can work with mysql

#fetching the temperature/humidity/time and append it to the array 
rows = cursor.fetchall()
for row in rows:
	result = row['temperature']
	temp.append(result)
	result1 = row['humidity']
	hum.append(result1)
	result2 = str(row['time'])
	tim.append(result2)

#make the x-axis the time stamp
x1 = tim 
#rotate so it doesn't look messy
plt.xticks(rotation=13)
#make the y-axis the temperature value
y1 = temp 
# plotting the temperature vs time points  
plt.plot(x1, y1, label = "temperature") 
  
# line 2 points 
x2 = tim 
y2 = hum 
# plotting the humidity vs time points  
plt.plot(x2, y2, label = "humidity") 
  
# naming the x axis 
plt.xlabel('time') 
# naming the y axis 
plt.ylabel('Temperature and Humidity') 
# giving a title to my graph 
plt.title('Temperature V.S. Humidity!') 
  
# show a legend on the plot 
plt.legend() 

# saving this graph so I can call it in php and display it on the web
plt.savefig('/var/www/html/chart.png')

# function to show the plot 
plt.show() 

cursor.close()
db.close()

