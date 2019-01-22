<?php
    /**Fetches all profiles from the database and outputs them as option blocks in a drop down menu.*/
	$column = 'name';
	while( $row = mysqli_fetch_assoc( $result ) ) //fetch the information from one row untill there are no more rows
	{
        echo '<option>'.$row[$column].'</option>';  //output option block with the name of the row
	}
?>