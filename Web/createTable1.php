<?php
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");

//$db->exec("CREATE TABLE 'usersWeb' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , 'username' VARCHAR(30) NOT NULL  UNIQUE , 'password' VARCHAR(64) NOT NULL , 'salt' VARCHAR(3))");


//$db->exec("CREATE TABLE 'HorarisFix' ('obre' DATETIME , 'tanca' DATETIME , 'lloc' VARCHAR(60), 'dia' VARCHAR(100))");
//$db->exec("CREATE TABLE 'HorarisVariables' ('Dia' DATETIME ,'obre' DATETIME , 'tanca' DATETIME , 'lloc' VARCHAR(60))");
//$db->exec("ALTER TABLE 'main'.'Log' ADD COLUMN 'Lloc' VARCHAR(60)");
/*
$db->exec("DELETE FROM tarja where NumeroTargeta = '090207'");
$db->exec("DELETE FROM tarja where NumeroTargeta = '090208'");
$db->exec("DELETE FROM tarja where NumeroTargeta = '090209'");
$db->exec("DELETE FROM tarja where NumeroTargeta = '090210'");
$db->exec("DELETE FROM tarja where codiTargeta = '1445077862126010'");
$db->exec("DELETE FROM tarja where codiTargeta = '1009253040224890'");

$db->exec("UPDATE tarja SET codiTargeta = '9460186227018756' where NumeroTargeta = '090203'");
$db->exec("UPDATE tarja SET codiTargeta = '8122182515655187' where NumeroTargeta = '090204'");
$db->exec("UPDATE tarja SET codiTargeta = '2713803530281003' where NumeroTargeta = '090205'");
$db->exec("UPDATE tarja SET codiTargeta = '1291703040224890' where NumeroTargeta = '090206'");
*/

$db->exec("UPDATE Usuaris SET Targeta = '9460186227018756' where Id = '5349'");
$db->exec("UPDATE Usuaris SET Targeta = '8122182515655187' where Id = '5350'");
$db->exec("UPDATE Usuaris SET Targeta = '2713803530281003' where Id = '5351'");
$db->exec("UPDATE Usuaris SET Targeta = '1291703040224890' where Id = '5352'");


$result = $db->query("Select * from tarja");
foreach($result as $row)
{
	print "IdUsuari ".$row['idUsuari']." NumeroTargeta ".$row['NumeroTargeta']." codiTargeta ".$row['codiTargeta']."<br>";
	
}


?>