<?
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
$result = $db->query("SELECT * FROM tarja where NumeroTargeta = '".$_GET["num"]."'");
$tarjeta = "";
foreach($result as $row)
	{	
		$tarjeta = $row['TempsP']."|".$row['TempsG']."|".$row['idUsuari'];
	}
	print $tarjeta;
?>