<?php
    //define options in drop down menu;

	while( $row = mysqli_fetch_assoc( $result ) )
	{
        echo '<option>'.$row[$column].'</option>';
	}
?>