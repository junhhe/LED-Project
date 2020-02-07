<?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "school";


//create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// check connection
if($conn->connect_error){
    die("connection failed:".$conn->connect_error);
}

//create variable and load/save SQL staement
$sql = "INSERT INTO students (name, age, gradeLevel)VALUES ('John', 14, 8)";
//taking our statement (sql) passing the query into the object because the object-
//handle all the back end
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?> 
