<?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "school";
$name = "jun";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
$sql = "SELECT*FROM students WHERE name ='jun'";
$result =$conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row['name']. " is " . $row['age']. " and in grade " . $row['gradeLevel'] ;
    }
} else {
    echo "0 results";
}
$conn->close();
?> 
