<?php
include("header.php");

//retrieve our data from POST
$nom = $_POST['nom'];
$cognom1 = $_POST['cognom1'];
$cognom2 = $_POST['cognom2'];
$direccio = $_POST['direccio'];
$poblacio = $_POST['poblacio'];
$provincia = $_POST['provincia'];
$cp = $_POST['cpostal'];
$telefon1 = $_POST['telefon'];
$telefon2 = $_POST['telefon2'];
$email = $_POST['email'];
$nif = $_POST['dni'];
$datanaix = $_POST['n_any']."-".$_POST['n_mes']."-".$_POST['n_dia']." 0:00:00";
$nacionalitat = $_POST['nacionalitat'];
$sexe = $_POST['sexe'];
$observacions = $_POST['observacions'];
$targeta = $_POST['targeta'];
$TempsP = $_POST["TPagament"];
$TempsG = $_POST["TGratis"];
$NumTarja = $_POST["NumTarja"];
$actiu = $_POST['actiu'];
try{
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
if ( isset($_POST["Id"])){
	$strUpdate = "UPDATE Usuaris SET Nom = '$nom',Cognom1 = '$cognom1',Cognom2='$cognom2' ,Direccio='$direccio',Poblacio='$poblacio',Provincia='$provincia',CP='$cp',Telefon1='$telefon1',Telefon2='$telefon2',Email='$email',NIF='$nif',DataNaix='$datanaix',Nacionalitat='$nacionalitat',Sexe='$sexe',Observacions='$observacions',Targeta='$targeta',Actiu=$actiu ";
	$strUpdate .= "Where Id = ".$_POST["Id"];
	// print $strUpdate;
	
	$db->exec($strUpdate);
	$strUpdate = "UPDATE tarja SET idUsuari = ".$_POST["Id"]." where codiTargeta = '".$targeta."' ";
	$db->exec($strUpdate);
} else {
	$strQuery = "INSERT INTO Usuaris ( Nom,Cognom1,Cognom2,Direccio,Poblacio,Provincia,CP,Telefon1,Telefon2,Email,NIF,DataNaix,Nacionalitat,Sexe,Observacions,Targeta,DataAlta,Actiu)";
	$strQuery .= "VALUES ( '$nom' , '$cognom1' , '$cognom2','$direccio','$poblacio','$provincia','$cp','$telefon1','$telefon2','$email','$nif','$datanaix','$nacionalitat','$sexe','$observacions','$targeta',datetime('now', 'localtime'),1);";
	$db->exec($strQuery);
	$result = $db->query("select last_insert_rowid();");
	//PRINT $strQuery;
	print " Usuari ".$nom." amb numero targeta ".$targeta." afegit a la BD ! ";
	foreach($result as $row)
	{
	$idUser =  $row[0];
	}
	$strUpdate = "UPDATE tarja SET idUsuari = ".$idUser." where codiTargeta = '".$targeta."' ";
	$db->exec($strUpdate);
}
if ( $targeta != "")
{
	$strUpdate = "UPDATE tarja SET idUsuari = ".$_POST["Id"].",TempsP=".$TempsP.",TempsG=".$TempsG.",NumeroTargeta='".$NumTarja."' where codiTargeta = '".$targeta."' ";
	//print $strUpdate;
	$db->exec($strUpdate);
}
} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}
header('Location: membersonly.php');
?>
