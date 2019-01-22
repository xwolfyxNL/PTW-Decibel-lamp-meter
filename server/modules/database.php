
<?php
    /**Initializes database with the name 'lampapplication' and the table profiles and puts the information
    *of the database in a variable.
    */
    $conn = mysqli_connect("localhost","root","","lampapplication"); // Database connection settings
    if(!$conn)
    {
        die("Connection failed: " . mysqli_connect_error()); // If the application can't connect to the database output an error
    }
    $sql = "SELECT * FROM profiles"; // Select all the data from the table provided above
    $result = $conn -> query($sql); // Put the result of the query in a variable
?>