<?php

//initialize database
$conn = mysqli_connect("localhost","root","","lampapplication");

if(!$conn)
{
die("Connection failed: " . mysqli_connect_error());
}

$result = $conn -> query("SELECT * FROM profielen");


?>