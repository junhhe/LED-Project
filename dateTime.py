#use the datetime object to create and manipulate date and time 
#resource: https://www.guru99.com/date-time-and-datetime-classes-in-python.html
from datetime import time 
from datetime import date
from datetime import datetime 

#create a main loop so this module can be imported 
def main():
	
	#create a new date time object that holds the current datetime 
	#make datetime an object (datetime.now)
	currentTime = datetime.now()
	print(currentTime)
	print(type(currentTime))
	
	#print only the time from the datetime object 
	print(datetime.time(currentTime))
	
	#use strftime to print only the year from the datetime object 
	print("current Year: ",currentTime.strftime("%Y"))
	
	#use strftime to print a very human readable date
	#% is string substitution just like the dollar sign in php
	print("Current Date: ",currentTime.strftime("%a, %B %d, %Y"))
	
	
if __name__ == "__main__":
	main()
