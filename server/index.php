


<?php
    include 'modules/database.php'; // Load the database module
?>
<?php
    // insert into database and reload page
    if(isset($_POST['save']))
    {
	//$sql
        $checkresult = mysqli_query($conn, "SELECT * FROM profiles WHERE name = '".$_POST['profilename']."'");
        $num_rows = mysqli_num_rows($checkresult);
        if($num_rows>0)
        {
            echo '<script language="javascript">';
            echo 'alert("Profile already exists!")';
            echo '</script>';
        }
        else
        {
      	    $sql0 = "INSERT INTO profiles (name, minimum, maximum)
      	    VALUES ('".$_POST["profilename"]."','".$_POST["minimum"]."','".$_POST["maximum"]."')";
     	    $result = mysqli_query($conn,$sql0);
	    header("Refresh:0");
	}
    }
    //delete from database and reload page
    if(isset($_POST['delete']) && $_POST['profiles'] != 'current' && $_POST['profiles'] != 'default')
    {
		$sql1 = "DELETE FROM profiles WHERE name = '".$_POST['profiles']."'";
		$result = mysqli_query($conn,$sql1);
		header("Refresh:0");
    }
    //update the current profile
    if (isset($_POST['use']))
    {
	    $sql2 = "SELECT minimum, maximum FROM profiles WHERE name = '".$_POST['profiles']."'";
	    $result0 = mysqli_query($conn, $sql2);
	    $values = mysqli_fetch_assoc($result0);
	    $min = $values['minimum'];
	    $max = $values['maximum'];
	    $sql3 = "UPDATE profiles SET minimum = ".$min.", maximum = ".$max." WHERE name = 'current'";
	    $result1 = mysqli_query($conn, $sql3);
	    header("Refresh:0");
    }
?>


<form method="post" >

<!––define drop down menu-->
	<select name = "profiles">


		//define options in drop down menu;
		<?php
		
		
		include 'modules/dropdown.php'; # Load the module dropdown
		?>
	</select>
	<input type = "submit" name = "delete" value = "Delete profile"/> <br>
	<input type = "submit" name = "use" value = "Use this profile"/>
    <br><br>

	<!--get user input-->
	Profilename: <br>
    <input type="text" name="profilename">
    <br><br>

    Highest dB value: <br>
    <input type="text" name="maximum">
    <br><br>

    Lowest dB value: <br>
    <input type="text" name="minimum" >
    <br><br>

    <input type="submit" name = "save" value = "Save new profile"/>

</form>