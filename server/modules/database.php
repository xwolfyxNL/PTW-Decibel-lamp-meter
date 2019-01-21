
<?php
    //initialize database
    $conn = mysqli_connect("localhost","root","",$database);
    if(!$conn)
    {
        die("Connection failed: " . mysqli_connect_error());
    }
    $sql = "SELECT * FROM ".$table;
    $result = $conn -> query($sql);
?>