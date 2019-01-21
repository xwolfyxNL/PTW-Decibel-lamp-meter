
<?php
//initialize database;
$conn = mysqli_connect("localhost","root","","LampAppProfiles");
if(!$conn)
{
die("Connection failed: " . mysqli_connect_error());
}
$result = $conn -> query("SELECT * FROM profielen");
?>

<?php
//insert into database and reload page
  if(isset($_POST['save']))
{
   	$sql0 = "INSERT INTO profielen (naam, minimaal, maximaal)
   	VALUES ('".$_POST["naam"]."','".$_POST["minimaal"]."','".$_POST["maximaal"]."')";
   	$result = mysqli_query($conn,$sql0);
	header("Refresh:0");
}
//delete from database and reload page
if(isset($_POST['delete']) && $_POST['profielen'] != 'ingesteld' && $_POST['profielen'] != 'default')
{
		$sql1 = "DELETE FROM profielen WHERE naam = '".$_POST['profielen']."'";
		$result = mysqli_query($conn,$sql1);
		header("Refresh:0");
}
if (isset($_POST['use']))
{
	$sql2 = "SELECT minimaal, maximaal FROM profielen WHERE naam = '".$_POST['profielen']."'";
	$result0 = mysqli_query($conn, $sql2);
	$values = mysqli_fetch_assoc($result0);
	$min = $values['minimaal'];
	$max = $values['maximaal'];
	$sql3 = "UPDATE profielen SET minimaal = ".$min.", maximaal = ".$max." WHERE naam = 'ingesteld'";
	$result1 = mysqli_query($conn, $sql3);
	header("Refresh:0");
}
?>


<form method="post" >

<!––define drop down menu-->
	<select name = "profielen">


		//define options in drop down menu;
		<?php
		while( $row = mysqli_fetch_assoc( $result ) )
		{
     		   echo '<option>'.$row['naam'].'</option>';
		}
		?>
	</select>
	<input type = "submit" name = "delete" value = "Delete profile"/> <br>
	<input type = "submit" name = "use" value = "Use this profile"/>
</form>


<br><br>

<?php
?>

<form method = "post">
Profielnaam: <br>
<input type="text" name="naam">
<br><br>

Hoge dB waarde: <br>
<input type="text" name="maximaal">
<br><br>

Lage dB waarde: <br>
<input type="text" name="minimaal" >
<br><br>

<input type="submit" name = "save" value = "Save new profile"/>

</form>
