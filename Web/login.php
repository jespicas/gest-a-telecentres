<?php
session_start(); //must call session_start before using any $_SESSION variables
$username = $_POST['username'];
$password = $_POST['password'];
//connect to the database here
//$username = mysql_real_escape_string($username);

try{
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
	$result = $db->query("SELECT password, salt FROM usersWeb WHERE username = '$username';");
	while($row=$result->fetch(SQLITE_ASSOC)){
		$hash = hash('sha256', $row['salt'] . hash('sha256', $password) );
		if($hash != $row['password']) //incorrect password
		{
			header('Location: login_form.php');
			die();
		}
		else
		{
			validateUser(); //sets the session data for this user
		}	
	}

} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}
header('Location: membersonly.php');
function validateUser()
{
    session_regenerate_id (); //this is a security measure
    $_SESSION['valid'] = 1;
   # $_SESSION['userid'] = $userid;
}
//redirect to another page or display "login success" message
?>