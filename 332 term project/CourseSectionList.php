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
	
	$Coursenum = $_POST["Cnum"];
	
$query = "SELECT Sect_Num, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, COUNT(Enroll_CWID)'numstudents'
	  FROM SECTION, ENROLLMENT, COURSE
	  WHERE Sect_Num = Enroll_Sect_Num
	  AND Course_Num = '$Coursenum'
	  AND Sect_Course_Num = Course_Num
	  GROUP BY Sect_Num";
	$result = mysqli_query($link,$query) or die('Could not connect query: ' . mysqli_error());
	$index = 0;
	if ($index < mysqli_num_rows($result))
	{		echo "Course Number: " .$_POST["Cnum"], "<BR>", "<BR>";
				while ($row = $result->fetch_assoc()) {
					echo "Section Number: ";
					echo $row['Sect_Num']. "<br>";
					echo "Section Classroom: ";
					echo $row['Sect_Classroom']."<br>";
					echo "Section Meeting Days: ";
					echo $row['Sect_Meeting_Days']."<br>";
					echo "Section Start time: ";
					echo $row['Sect_Begin_Time']."<br>";
					echo "Section End time: ";
					echo $row['Sect_End_Time']."<br>", "<br>";
					echo "Enrolled Students Count: ";
					echo $row['numstudents'], "<br>", "<br>";
  
												}
	}
	else{ 
	echo "Error!", "<BR>", "invalid Social Security Number present, Please enter a valid SSN.","<BR>"; 
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
          
