<html>
<body>
<div id="main">
   <style>
   h1 {text-align: center;}
   h2 {text-align: center;}
   </style>
   <h1>CPSC 332 2021 Term Project</h1>
   <h2>by: Richard Gresham</h2><br>
</div>

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
	
	$Coursenum = $_POST["coursenum"];
	$Sectnum = $_POST["sectnum"];

	$query = "SELECT COUNT(*) 'numberofgrades', Grade
         FROM COURSE,SECTION,ENROLLMENT
         WHERE Course_Num = Sect_Course_Num
         AND Enroll_Course_Num = Course_Num
         AND Enroll_Sect_Num = Sect_Num
         AND Sect_Num = '$Sectnum'
         AND Course_Num = '$Coursenum'
         GROUP BY Grade";

	$result = mysqli_query($link,$query) or die('Could not connect: ' . mysqli_error());
	$index = 0;
	if ($index < mysqli_num_rows($result))
	{		echo "Course Number: " .$_POST["coursenum"], "<BR>";
			echo "Section Number: " .$_POST['sectnum'], "<BR>";
			while ($row = $result->fetch_assoc()) {
				echo $row['numberofgrades'];
				echo " Student(s) received a: ".$row['Grade'], "<BR>";  
												}
	}
	else{ 
	echo "Error!", "<BR>", "invalid Social Security Number present, Please enter a valid SSN.","<BR>"; 
    	}

	// Close Database
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
