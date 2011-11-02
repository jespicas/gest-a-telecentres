<? include("header.php");
?>
<link href="style.css" rel=StyleSheet type=text/css>

<script>
    function Collapse(id)
{
	if ( document.getElementById(id).style.visibility == "collapse"){
	document.getElementById(id).style.visibility = "visible";
	document.getElementById(id).style.display = "inline";
	} else {
	document.getElementById(id).style.visibility = "collapse";
	document.getElementById(id).style.display = "none";
	}
}
	function Paginacio(NumPagina)
	{
		document.getElementById("pagina").value = NumPagina;
		Llistat.submit();
	}
	function CanviTarja(str)
	{
	  	index = str.selectedIndex;
		valor = str.options[index].text;
		numero = valor.split('|')[0];
	if (str=="")
	  {
	 // document.getElementById("txtHint").innerHTML="";
	  return;
	  }
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
	  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
		TempsP = xmlhttp.responseText.split('|')[0];
		TempsG = xmlhttp.responseText.split('|')[1];
		document.getElementById("NumTarja").value = numero;
		document.getElementById("TGratis").value = TempsG;
		document.getElementById("TPagament").value = TempsP;
		
		//alert(xmlhttp.responseText);
		//document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
		}
	  }

	xmlhttp.open("GET","gettarja.php?num="+numero,true);
	xmlhttp.send();
	}
	/*
	function CanviTarja(str)
	{
		index = str.selectedIndex;
		valor = str.options[index].text;
		numero = valor.split('|')[0];
		alert(numero);
		document.getElementById("NumTarja").value = numero;
		document.getElementById("TGratis").value = 90;
	}
	*/
	function enviar()
	{

		var error_trobat=0;
	
		if(afegir.nom.value=="")
		{
			alert("El nom és una dada obligatoria.");
			afegir.nom.focus();			
			error_trobat=1;
		}
		else if(afegir.cognom1.value=="")
		{
			alert("El primer cognom és una dada obligatoria.");
			afegir.cognom1.focus();			
			error_trobat=1;		
		}
		else if(afegir.dni.value=="")
		{
			alert("El dni és una dada obligatoria.");
			afegir.dni.focus();			
			error_trobat=1;		
		}
		else if( (afegir.n_dia.value=="") || (afegir.n_mes.value=="") || (afegir.n_any.value==""))
		{
			alert("La data de naixement és una dada obligatoria.");
			afegir.n_dia.focus();			
			error_trobat=1;				
		}	
		else if(afegir.targeta.value=="")
		{
			alert("La targeta és una dada obligatoria.");
			afegir.targeta.focus();			
			error_trobat=1;		
		}		
		if(error_trobat==0) 
		{		
			afegir.submit();
		}		
	}
	
</script>
<?
include("menu.php");

//page content follows
try{
//$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
//$result = $db->query("SELECT * FROM Log");
if (isset($_GET["Del"]))
{ DelUsuari();
}
?>

<div class="fonsMenuPpal" ><a href="#" onclick="javascript:Collapse('AddUsers');Collapse('LlistaUsuaris');" >Affegir nou usuari</a></div>
<form action="membersonly.php" method="post" enctype="multipart/form-data" name="Llistat" id="Llistat">
<div id="Busca" class="taulaFormInterior">
	<table>
	<tr>
	<td>Nom:</td><td><input name="nomBusca" type="text" class="input" id="nomBusca" value="<? if (isset($_POST["nomBusca"])){ print $_POST["nomBusca"];} ?>" size="30" maxlength="30"></td>
	</tr>
	<tr>
	<td>Cognom:</td><td><input name="cognomBusca" type="text" class="input" id="cognomBusca" value="<? if (isset($_POST["cognomBusca"])){ print $_POST["cognomBusca"];} ?>" size="30" maxlength="30"></td>
	<tr>	
	<td>NumTarja</td><td><input name="NumTarjaBusca" type="text" class="input" id="NumTarjaBusca" value="<? if (isset($_POST["NumTarjaBusca"])){ print $_POST["NumTarjaBusca"];} ?>" size="30" maxlength="30"></td>
	</tr>
	<tr>
	<td>IdTarja</td><td><input name="IdTarjaBusca" type="text" class="input" id="IdTarjaBusca" value="<? if (isset($_POST["IdTarjaBusca"])){ print $_POST["IdTarjaBusca"];} ?>" size="30" maxlength="30"></td>
	</tr>
	<tr>
	<td></td><td><input type="submit" class="inputBoto" /></td>
	</tr>	
	</table>
</div>
<span class="space">&nbsp;</span>
<div id="LlistaUsuaris" <? if (isset($_GET["Id"])){ print "style=\"visibility:collapse;\"";} else { print "style=\"visibility:visible;\"";} ?>>
	<? print PaginacioControl() ?>
	
	<input Id="pagina" name="pagina" type="hidden" >
	<table class='taulaFormInterior'>
	<tr >
	<td class="textForm20">Mod</td><td class="textForm20">Del</td><td class="textForm20">Nom</td><td class="textForm20">Cognom</td><td class="textForm20">E-mail</td></td><td class="textForm20">IdTarja</td><td class="textForm20">Actiu</td>
	</tr>
	<? print LlistaUsuaris() ?>
	</table>

	<? print PaginacioControl() ?>
	<br>
</div>
</form>	
	<div id="AddUsers" <? if (isset($_GET["Id"])){ print "style=\"visibility:visible;\"";} else { print "style=\"visibility:collapse;\"";} ?>>
	<form action="Addusuaris.php" method="post" enctype="multipart/form-data" name="afegir" id="afegir">
	<input name="idioma" type="hidden" value="1">
	<? if (isset($_GET["Id"])){ print '<input name="Id" type="hidden" value="'.$_GET["Id"].'">';} else { print "";} ?>
        <table width="90%" border="0" cellpadding="3" cellspacing="2" align="center" class="taulaFormInteriorAddUser">
          <tr> 
            <td colspan="2" align="center" class="errroNick">&nbsp;&nbsp;</td>
          </tr>
          <tr> 
            <td width="40%" align="right" ><strong>Nom</strong>&nbsp;</td>
            <td width="60%" align="left" valign="top"><input name="nom" type="text" class="input" id="nom" value="<? print Get("Nom"); ?>" size="30" maxlength="30">            </td>
          </tr>
          <tr> 
            <td align="right" ><strong>Primer cognom</strong>&nbsp;</td>
            <td align="left" valign="top"><input name="cognom1" type="text" class="input" id="cognom1" value="<? print Get("Cognom1"); ?>" size="30" maxlength="30"></td>
          </tr>
          <tr> 
            <td align="right" >Segon cognom&nbsp;</td>
            <td align="left" valign="top"><input name="cognom2" type="text" class="input" id="cognom2" value="<? print Get("Cognom2"); ?>" size="30" maxlength="15"></td>
          </tr>
          <tr> 
            <td align="right" >Adre&ccedil;a&nbsp;</td>
            <td align="left" valign="top"><input name="direccio" type="text" class="input" id="direccio" value="<? print Get("Direccio"); ?>" size="40" maxlength="40"></td>
          </tr>
          <tr> 
            <td align="right" >Poblaci&oacute;&nbsp;</td>
            <td align="left" valign="top"><input name="poblacio" type="text" class="input" id="poblacio" value="<? print Get("Poblacio"); ?>" size="40"></td>
          </tr>
          <tr> 
            <td align="right" >Prov&iacute;ncia&nbsp;</td>
            <td align="left" valign="top"><input name="provincia" type="text" class="input" id="provincia" value="<? print Get("Provincia"); ?>" size="30" maxlength="15"></td>
          </tr>
          <tr> 
            <td align="right" ><strong>Codi postal</strong>&nbsp;</td>
            <td align="left" valign="top"><input name="cpostal" type="text" class="input" id="cpostal" value="<? print Get("CP"); ?>" size="6" maxlength="5"></td>
          </tr>
          <tr> 
            <td align="right" >Tel&egrave;fon 1</td>
            <td align="left" valign="top"><input name="telefon" type="text" class="input" id="telefon" value="<? print Get("Telefon1"); ?>" size="15" maxlength="12"></td>
          </tr>
          <tr> 
            <td align="right" >Tel&egrave;fon 2</td>
            <td align="left" valign="top"><input name="telefon2" type="text" class="input" id="telefon2" value="<? print Get("Telefon2"); ?>" size="15" maxlength="12"></td>
          </tr>
          <tr> 
            <td align="right" >Correu electr&ograve;nic</td>
            <td align="left" valign="top"><input name="email" type="text" class="input" id="email" value="<? print Get("Email"); ?>" size="50">            </td>
          </tr>
          <tr> 
            <td align="right" ><strong>NIF</strong>&nbsp;</td>
            <td align="left" valign="top"><input name="dni" type="text" class="input" id="dni" value="<? print Get("NIF"); ?>" size="11" maxlength="20">
              </td>
          </tr>		  
          <tr> 
            <td align="right" ><strong>Data de naixement</strong>&nbsp;</td>
            <td align="left" valign="top">
			<? print GetDataNaix(); ?>
			&nbsp;<span class="input">(dd-mm-aaaa)</span></td>
          </tr>
		  <tr> 
            <td align="right" >Nacionalitat&nbsp;</td>
            <td align="left" valign="top"><input name="nacionalitat" type="text" class="input" id="nacionalitat" value="<? print Get("Nacionalitat"); ?>" size="40" maxlength="100"></td>
          </tr>		  
          <tr> 
            <td align="right" >Sexe&nbsp;</td>
            <td align="left" valign="top"><select name="sexe" id="sexe">
			                <option value="H" <? if (Get("Sexe") == "H") { print "selected";} ?>>Home</option>
                <option value="D" <? if (Get("Sexe") == "D") { print "selected";} ?>>Dona</option>
              </select></td>
          </tr>		  	  		  
          <tr> 
            <td align="right" ">Observacions&nbsp;</td>
            <td align="left" valign="top"><textarea name="observacions" cols="50" rows="3" class="input" id="observacions"><? print Get("Observacions"); ?></textarea></td>
          </tr>

          <tr> 
            <td align="right" >&nbsp;</td>
            <td align="left" valign="top">&nbsp;</td>
          </tr>
          <tr> 
            <td align="right"><strong>Targeta</strong>&nbsp;</td>
            <td align="left" valign="top"><? if(isset($_GET["Id"])){ print GetTargesLliures(Get("Targeta")); } else {print GetTargesLliures("");}?></td>
          </tr>
          <tr> 
            <td align="right">&nbsp;</td>
            <td align="left" valign="top">
			<table>
				<tr><td>T. Pagament</td><td>T. Gratuit</td><td>NumTarga</td>
				</tr>
				<tr>
				<td><input name="TPagament" type="text" class="input" id="TPagament" value="<? print Get("TempsP"); ?>" size="20" maxlength="50"></td>
				<td><input name="TGratis" type="text" class="input" id="TGratis" value="<? print Get("TempsG"); ?>" size="20" maxlength="50"></td>
				<td><input name="NumTarja" type="text" class="input" id="NumTarja" value="<? print Get("NumeroTargeta"); ?>" size="40" maxlength="100"></td>
				</tr>
			</table>
			</td>
          </tr>		  
          <tr> 
            <td align="right" >Actiu</td>
            <td align="left" valign="top"><input name="actiu" type="text" class="input" id="actiu" value="<? print Get("Actiu"); ?>" size="40" maxlength="100"></td>
          </tr>		  		  
          <tr align="center"> 
            <td colspan="2"><a href="javascript:enviar();" class="butoAfegir">&nbsp;Guardar 
              dades&nbsp;</a>&nbsp;<a href="membersonly.php?pagina=<? if (isset($_GET["pagina"])){ print $_GET["pagina"];} else { print "0";} ?>">Tornar</a> </td>
          </tr>
        </table>
        <br>
	</form>
</div>	
<?

} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}

function DelUsuari()
{
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
	if (isset($_GET["Id"])){
	      $count = $db->exec("DELETE FROM Usuaris where Id = ".$_GET["Id"]);
		  $count = $db->exec("UPDATE tarja SET idUsuari = NULL  where IdUsuari = ".$_GET["Id"]);
		  
	}
}
function LlistaUsuaris()
{
$registres = 25;

$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");

if ( isset($_GET["pagina"]))
{
$Pagina = $_GET["pagina"];
} else {
if ( isset($_POST["pagina"])){
	if ( $_POST["pagina"] != "")
	{
		$Pagina = $_POST["pagina"];
	} else {
		$Pagina = 0;
	}
} else {
$Pagina = 0;
}

}

if (!$Pagina )
{
	$inici = 0;
	$Pagina = 1;
} else {
$inici = ($Pagina -1 ) * $registres;
}
$query = "";
if ( isset($_POST["nomBusca"]))
{
	if ( $_POST["nomBusca"] != ""){
	$query .= "Nom = '".$_POST["nomBusca"]."'";
	}
}
if ( isset($_POST["cognomBusca"]) )
{
	if( $_POST["cognomBusca"] != ""){
	$query .= " Cognom1 = '".$_POST["cognomBusca"]."'";
	}
}
if ( isset($_POST["IdTarjaBusca"]) )
{
	if ( $_POST["IdTarjaBusca"] != "" ){
	$query .= " Targeta = '".$_POST["IdTarjaBusca"]."'";
	}
}

if ( $query != "")
{
$query = "where ".$query;
}
$res = $db->query("Select count(*) from Usuaris ".$query);
$total_registre = $res->fetchColumn();
$strQuery = "Select * from Usuaris ".$query." LIMIT ".$inici.",".$registres;
$result = $db->query($strQuery);
$total_pagines = ceil($total_registre / $registres);
//print $strQuery;
$html = "";
foreach($result as $row)
{
$html .= '<tr>';
$html .= '<td class="trColor2"><a href="membersonly.php?pagina='.$Pagina.'&Id='.$row['Id'].'">M</a></td>';
$html .= '<td class="trColor2"><a href="membersonly.php?pagina='.$Pagina.'&Id='.$row['Id'].'&Del=1">D</a></td>';
$html .= '<td class="trColor1">'.$row['Nom'].'</td>';
$html .= '<td class="trColor1">'.$row['Cognom1'].'</td>';
if ($row['Email']  == ""){$email = "&nbsp;";} else { $email = $row['Email'];}
$html .= '<td class="trColor1">'.$email.'</td>';
if ($row['Targeta'] == ""){$tarjeta = "&nbsp;";} else { $targeta = $row['Targeta'];}
$html .= '<td class="trColor1">'.$targeta.'</td>';
$html .= '<td class="trColor1">'.$row['Actiu'].'</td>';
$html .= '</tr>';
$email = "";
$targeta="";
}
return $html;
}
function GetDataNaix()
{
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
	if ( isset($_GET["Id"])){
	$res = $db->query("Select DataNaix from Usuaris where Id =".$_GET["Id"]);
	foreach($res as $row)
	{
		$data = $row["DataNaix"];
	}
	$data = str_replace("0:00:00","",$data);
	
	list($day,$month,$year) = split('[/.-]', $data);
	
		$html = '<select name="n_dia">';
		for ( $i =1; $i <= 31; $i++){
			if ( $i == $day ) {
			$html .="<option  selected value=".$i.">".$i."</option>";
			} else {
			$html .="<option  value=".$i.">".$i."</option>";
			}
			}
		$html .= '</select>-';
		$html .= '<select name="n_mes">';
		for ( $i =1; $i <= 12; $i++){
			if ($i == $month){
			$html .="<option  selected value=".$i.">".$i."</option>";
			} else {
			$html .= "<option  value=".$i.">".$i."</option>";
			}
		}
		$html .= '</select>-';
		$html .= '<select name="n_any">';
		$any = getdate();
		$any = $any["year"] - 14;
		for ( $i = 1905; $i <= $any; $i++)
		{
			if  ( $i == $year)
			{
			$html .="<option  selected value=".$i.">".$i."</option>";
			} else {
			$html .= "<option  value=".$i.">".$i."</option>";
			}
		}
		$html .= "</select";
	return $html;
	} else {
	    $html = '<select name="n_dia">';
		for ( $i =0; $i <= 31; $i++){
			$html .="<option  value=".$i.">".$i."</option>";
			}
		$html .= '</select>-';
		$html .= '<select name="n_mes">';
		for ( $i =1; $i <= 12; $i++){
			$html .= "<option  value=".$i.">".$i."</option>";
		}
		$html .= '</select>-';
		$html .= '<select name="n_any">';
		$any = getdate();
		$any = $any["year"] - 14;
		for ( $i = 1905; $i <= $any; $i++)
		{
			$html .= "<option  value=".$i.">".$i."</option>";
		}
		$html .= "</select";
		return $html;
	}
}
function Get($value)
{
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
	if ( isset($_GET["Id"])){
	$res = $db->query("Select * from Usuaris inner join tarja on Usuaris.Id = tarja.idUsuari where Usuaris.Id =".$_GET["Id"]);
	foreach($res as $row)
	{
		$Usuari = $row[$value];
	}
	if ($Usuari == "")
	{
		$res = $db->query("Select * from Usuaris where Id =".$_GET["Id"]);
		foreach($res as $row)
		{
			$Usuari = $row[$value];
		}
	}
	return $Usuari;
	} else {
		return "";
	}
}
function PaginacioControl()
{
	$registres = 25;

	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
if ( isset($_GET["pagina"]))
{
$Pagina = $_GET["pagina"];
} else {
 if ( isset($_POST["pagina"])){
	if ( $_POST["pagina"] != "")
	{
		$Pagina = $_POST["pagina"];
	} else {
		$Pagina = 0;
	}
} else {
$Pagina = 0;
}
}
	if (!$Pagina )
	{
		$inici = 0;
		$Pagina = 1;
	} else {
		$inici = ($Pagina -1 ) * $registres;
	}
$query = "";
if ( isset($_POST["nomBusca"]))
{
	if ( $_POST["nomBusca"] != ""){
	$query .= "Nom = '".$_POST["nomBusca"]."'";
	}
}
if ( isset($_POST["cognomBusca"]) )
{
	if( $_POST["cognomBusca"] != ""){
	$query .= " Cognom1 = '".$_POST["cognomBusca"]."'";
	}
}
if ( isset($_POST["IdTarjaBusca"]) )
{
	if ( $_POST["IdTarjaBusca"] != "" ){
	$query .= " Targeta = '".$_POST["IdTarjaBusca"]."'";
	}
}

if ( $query != "")
{
$query = "where ".$query;
}
	$res = $db->query("Select count(*) from Usuaris ".$query);
	//print "Select count(*) from Usuaris ".$query;
	$total_registre = $res->fetchColumn();
	$total_pagines = ceil($total_registre / $registres);
	$html = "<center><table class='taulaFormInteriorPaginacio' ><tr>";
	$html .= "<td class='textForm20'><a href='javascript:Paginacio(0)'>|<</a><td>";
	if(($Pagina-1) > 0) {
		$html .= "<td class='textForm20'>Pàgina <a href='javascript:Paginacio(".($Pagina-5).")'>< ... </a></td>";
	}
	
	for ( $i = 1; $i <= $total_pagines; $i++)
	{
				
		if ($Pagina == $i) {
			$html .= "<td class='textForm21'>Pàgina ".$Pagina."</td>";
			} else {
			if ( $i < ($Pagina+ 5) & $i > ($Pagina - 5))
				$html .= "<td class='textForm20'>Pàgina <a href='javascript:Paginacio(".$i.")'>".$i."</a></td>";
			}

	}
	if(($Pagina + 1)<=$total_pagines) {
		$html .= "<td class='textForm20'> <a href='javascript:Paginacio(".($Pagina+5).")'>... ></a></td>";
	}
	$html .= "<td class='textForm20'><a href='javascript:Paginacio(".$total_pagines.")'>>| </a></td>";
	$html .= "</tr></table></center>";
	return $html;
}


function GetTargesLliures($tarja)
{
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
$result = $db->query("SELECT * FROM tarja where idUsuari IS NULL");
$html = '<select name = "targeta" onchange="CanviTarja(this);"><option value=""</option>';
foreach($result as $row)
	{	
	$html.='<option value='.$row['codiTargeta'].'>'.$row['NumeroTargeta'].'|'.$row['codiTargeta'].'</option>';
	}
	
	if ( $tarja != "" )
	{
		$result = $db->query("SELECT * FROM tarja where codiTargeta = '".$tarja."'");
		foreach($result as $row)
		{
		$html.='<option selected value='.$row['codiTargeta'].'>'.$row['NumeroTargeta'].'|'.$row['codiTargeta'].'</option>';
		}
	}
	$html .="</select>";
	return $html;
}

?>
