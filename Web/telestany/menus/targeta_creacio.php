<?
/*
TARGETA EXISTENT:
GET /telestany/menus/targeta_creacio.php?tipus=2&minuts=60&targeta=1250222427994134&numero=0000001 HTTP/1.1
RESPOSTA TEXT PLA: Error: Numero de targeta ja en us.

TARGETA NOVA:
GET /telestany/menus/targeta_creacio.php?tipus=2&minuts=60&targeta=5514758719231965&numero=141414 HTTP/1.1
RESPOSTA TEXT PLA: 2848
*/
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
if ( isset($_GET["targeta"]) & isset($_GET["numero"]))
{
$Query = "select * from tarja where NumeroTargeta = '".$_GET["numero"]."' or codiTargeta = '".$_GET["targeta"]."';";
//print $Query;
$result = $db->query($Query);

$quants = $result->fetchColumn();
//print $quants."...";
if ($quants > 0) {
print "Error: Numero de targeta ja en us.";
} else {
	$strQuery = "INSERT INTO tarja ( TempsP,TempsG,QImpressio,NumeroTargeta,codiTargeta)";
	$strQuery .= "VALUES ( 0 ,90 , 0,'".$_GET["numero"]."','".$_GET["targeta"]."');";
	$db->exec($strQuery);
print "1234";
}

}

?>