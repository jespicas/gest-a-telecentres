<?php
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");

//$db->exec("CREATE TABLE 'usersWeb' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , 'username' VARCHAR(30) NOT NULL  UNIQUE , 'password' VARCHAR(64) NOT NULL , 'salt' VARCHAR(3))");


//$db->exec("CREATE TABLE 'HorarisFix' ('obre' DATETIME , 'tanca' DATETIME , 'lloc' VARCHAR(60), 'dia' VARCHAR(100))");
//$db->exec("CREATE TABLE 'HorarisVariables' ('Dia' DATETIME ,'obre' DATETIME , 'tanca' DATETIME , 'lloc' VARCHAR(60))");
//$db->exec("ALTER TABLE 'main'.'Log' ADD COLUMN 'Lloc' VARCHAR(60)");

$result = $db->query("Select * from tarja");
foreach($result as $row)
{
	print "IdUsuari ".$row['idUsuari']." NumeroTargeta ".$row['NumeroTargeta']." codiTargeta ".$row['codiTargeta']."<br>";
	
}


?>