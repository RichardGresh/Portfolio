<html>
<body>
<div id="main">
   <style>
   h1 {text-align: center;}
   h2 {text-align: center;}
   </style>
   <h1>CPSC 332 2021 Term Project</h1>
   <h2>by: Richard Gresham</h2><br>
<div style="background-color:lightblue;">
<fieldset>
<legend>Student Grade Display:</legend>
<?php
	
	$link = mysqli_connect('mariadb', 'cs332t16', '5zMFS6no');
	if (!$link) {
			echo'issues found <p>';
			die('Could not connect: ' . mysqli_error());
		    }

	mysqli_select_db($link, 'cs332t16');
	echo 'Connected successfully to Database<p>';
	
	$CWID = $_POST["cwid"];
	

$query = "SELECT Enroll_Course_Num, Enroll_Sect_Num, Grade, Course_Title
    From ENROLLMENT, COURSE
	WHERE Enroll_Course_Num = Course_Num
	AND Enroll_CWID = '$CWID'";

	$result = mysqli_query($link,$query) or die('Could not connect query: ' . mysqli_error());
	$index = 0;
	if($index < mysqli_num_rows($result))
	{  echo "Student CWID: ".$_POST['cwid'], "<BR>", "<BR>";
	   while ($row = $result -> fetch_assoc()) {
			echo "Class: ";
			echo $row['Course_Title']. "<br>";
			echo "Course Number: ";
			echo $row['Enroll_Course_Num']. "<br>";
			echo "Section Number: ";
			echo $row['Enroll_Sect_Num']. "<br>";
			echo "Grade: ";
			echo $row['Grade']. "<br>", "<br>";
						}
	}

			
	   

		mysqli_close($link);

?>

<button onclick="previouspage()">return</button>

<script>
function previouspage() {
    window.history.back();
}
</script>

</fieldset>
</div>
</body>
</html>
