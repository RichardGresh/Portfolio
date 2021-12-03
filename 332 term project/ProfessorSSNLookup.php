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
<legend>Prof SSN Lookup:</legend>
<?php
	
	$link = mysqli_connect('mariadb', 'cs332t16', '5zMFS6no');
	if (!$link) {
			echo'issues found <p>';
			die('Could not connect: ' . mysqli_error());
		    }

	mysqli_select_db($link, 'cs332t16');
	echo 'Connected successfully to Database<p>';
	
	$PSSN = $_POST["ssn"];
	
	$query = "SELECT Course_Title, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time
          	FROM PROFESSOR, COURSE, SECTION
          	WHERE Prof_SSN = Sect_Prof_SSN
          	AND Sect_Course_Num = Course_Num
		AND Prof_SSN = $PSSN";
	$result = mysqli_query($link,$query) or die('Could not connect: ' . mysqli_error());
	$index = 0;
	if ($index < mysqli_num_rows($result))
	{		echo "Professor SSN: " .$_POST["ssn"], "<BR>", "<BR>";
			while ($row = $result->fetch_assoc()) {
				echo "Course Name: ";
    				echo $row['Course_Title']."<br>";
				echo "Classroom: ";
				echo $row['Sect_Classroom']."<br>";
				echo "Meeting Days: ";
				echo $row['Sect_Meeting_Days']."<br>";
				echo "Begin Time: ";
				echo $row['Sect_Begin_Time']."<br>";
				echo "End Time: ";
				echo $row['Sect_End_Time']."<br>","<br>";

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
          
          
          
          
