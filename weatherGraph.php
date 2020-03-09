<?php
$servername = "192.168.0.205";
$username = "humid";
$password = "password";
$dbname = "sensor";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connectionmysqli
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//selecting imformation from the database 
$sql = "SELECT * FROM weather ORDER BY time DESC";

//select time from the database in descending order 
$sql2 = "SELECT time FROM weather ORDER BY time DESC";
$result2 = $conn->query($sql2);
//output the most recent time because it's in descending order 
if ($result2->num_rows>0){
	while($row2 = $result2->fetch_assoc()) {
		$time = $row2["time"];
	}
}

// covert time to unix 
$x = strtotime($time);
//echo $x;
$result = $conn->query($sql);

//array for time, temperature, and humidity
$tim = array();
$tempe = array();
$humi = array();

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        //echo "Temperature: " . $row["temperature"]. "°C - Humidity: " . $row["humidity"]."%" ." " . $row["time"];
     
        //get the temperature and append it to the array with time
        array_push($humi, $row['humidity']." at ".$row['time']);
        //get the humidity and append it to the array with time
        array_push($tempe, $row['temperature']. " at " . $row['time']);
        //array_push($tim, $row['time']);
    }
} 
else {
    echo "0 results";
}

//display the image
echo "<img src='chart.png' />";
// get the max/min value that has a time stamp appending to it 
echo "</br>". "The max temperature is " . max($tempe);
echo "</br>". "The minimum temperature is " . min($tempe);
echo "</br>". "The max humidity is " . max($humi) ;
echo "</br>". "The minimum humidity is " . min($humi);

$date2 = mktime(); //current time in unix

//subtracting current time to the most current time in the database
$totalTime =  $date2 - $x;
//echo $totalTime;

//if the total time is greater than 300 seconds then it will send an alert saying it hasn't been updated
if ($totalTime > 300) {
	echo "</br> Update notification: no data has been received in more than 5 minutes. "; 
	}
else {
}

$conn->close();
?>
