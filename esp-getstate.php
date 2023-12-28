<!DOCTYPE html>
<html><body>
<?php

// REPLACE with your IP
$servername = "localhost";
// REPLACE with your Database name
$dbname = "yourDDBBname";
// REPLACE with Database user
$username = "databaseuser";
// REPLACE with Database user password
$password = "databasepass";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, dev_name, dev_code, status FROM YOURTABLENAME ORDER BY id ASC";

if ($result = $conn->query($sql)) {
    while($row = $result->fetch_assoc()){
        echo "Device: " . $row["dev_name"] . " Status: " . $row["dev_code"] ."". $row["status"] . "<br>";
    }
    $result->free();
}else{
    echo "0 results";
}

$conn->close();
?> 
</body>
</html>
