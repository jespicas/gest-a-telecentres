<?
include("header.php");

?>
<head>
	<link href="style.css" rel=StyleSheet type=text/css>
	<link type="text/css" rel="stylesheet" href="dhtmlgoodies_calendar/dhtmlgoodies_calendar.css?random=20051112" media="screen"></LINK>
	<SCRIPT type="text/javascript" src="dhtmlgoodies_calendar/dhtmlgoodies_calendar.js?random=20060118"></script>
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
		function Accio(obre,tanca,lloc,accio,dies,Id)
		{
		document.getElementById("obreh").value = obre;
		document.getElementById("tancah").value = tanca;
		document.getElementById("lloch").value = lloc;
		document.getElementById("diesh").value = dies;
		document.getElementById("hfixAccio").value = accio;
		document.getElementById("hfixId").value = Id;
		horaris.submit();
		}
		function AccioV(dia,obre,tanca,lloc,accio,Id)
		{
		document.getElementById("diahv").value = dia;
		document.getElementById("obrehv").value = obre;
		document.getElementById("tancahv").value = tanca;
		document.getElementById("llochv").value = lloc;
		document.getElementById("hvAccio").value = accio;
		document.getElementById("hvId").value = Id;
		horaris.submit();
		}
		
	</script>
</head>
<? include("menu.php"); 
if (isset($_POST["Lloc"])){
$Lloc = $_POST["Lloc"];
}
if(isset($_POST['Envia'])){
 $Dia = $_POST["day2"]."/".$_POST["month2"]."/".$_POST["year2"];
 $entra = $_POST["hour2"].":".$_POST["minute2"];
 $tanca = $_POST["hour3"].":".$_POST["minute3"];
 try{
	if ( $Lloc != ""){
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
 	$strQuery = "INSERT INTO HorarisVariables ( Dia,obre,tanca,lloc)";
	$strQuery .= "VALUES ( '$Dia' , '$entra' , '$tanca','$Lloc')";
//	print $strQuery;
	$db->exec($strQuery);
	}
} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}
}
if ( isset($_POST["HFix"])){

$HoraEntra = $_POST["hourEntra"].":".$_POST["minuteEntra"];
$HoraSurt = $_POST["hourSurt"].":".$_POST["minuteSurt"];
 try{
	if ( $Lloc != ""){
	$dies = "";
	if (isset($_POST["Dilluns"])) { $dies .= "Dilluns,";}
	if (isset($_POST["Dimarts"])) { $dies .= "Dimarts,";}
	if (isset($_POST["Dimecres"])) { $dies .= "Dimecres,";}
	if (isset($_POST["Dijous"])) { $dies .= "Dijous,";}
	if (isset($_POST["Divendres"])) { $dies .= "Divendres,";}
	if (isset($_POST["Dissabte"])) { $dies .= "Dissabte,";}
	if (isset($_POST["Diumenge"])) { $dies .= "Diumenge,";}
    $dies = substr($dies,0,strlen($dies) -1 );
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
 	$strQuery = "INSERT INTO HorarisFix ( obre,tanca,lloc,dia)";
	$strQuery .= "VALUES ( '$HoraEntra' , '$HoraSurt','$Lloc','$dies')";
//	print $strQuery;
	$db->exec($strQuery);
	}

} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}


}
if ( isset($_POST["hfixAccio"]))
{

	if ($_POST["hfixAccio"] == "HoresFixModifica")
	{
		Print " Modificar Hores Fix... amb dades antigues ".$_POST["obreh"]." ".$_POST["tancah"]."  ".$_POST["lloch"]."  ".$_POST["diesh"];
		print " <br>";
		print " Per Hores Noves ".$_POST["obre".$_POST["hfixId"]]."  ".$_POST["tanca".$_POST["hfixId"]]."  ".$_POST["lloc".$_POST["hfixId"]]."  ".$_POST["dies".$_POST["hfixId"]];
		 try{
		$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
		$strQuery = "UPDATE HorarisFix SET obre='".$_POST["obre".$_POST["hfixId"]]."',tanca='".$_POST["tanca".$_POST["hfixId"]]."',lloc='".$_POST["lloc".$_POST["hfixId"]]."',dia='".$_POST["dies".$_POST["hfixId"]]."'  where obre ='".$_POST["obreh"]."' and tanca ='".$_POST["tancah"]."' and lloc ='".$_POST["lloch"]."' and dia = '".$_POST["diesh"]."'";
//		print $strQuery;
		$db->exec($strQuery);

		} catch (PDOException $e)
		{
			echo $e->getMessage();
			echo "<br><br>Database -- NOT -- loaded successfully .. ";
			die( "<br><br>Query Closed !!! $error");
		}
	}
	if ($_POST["hfixAccio"] == "HoresFixElimina")
	{
		Print " Esborrar Hores Fix... amb dades antigues ".$_POST["obreh"]." ".$_POST["tancah"]."  ".$_POST["lloch"];
		 try{
		$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
		$strQuery = "DELETE FROM HorarisFix  where obre ='".$_POST["obreh"]."' and tanca ='".$_POST["tancah"]."' and lloc ='".$_POST["lloch"]."'";
	//	print $strQuery;
		$db->exec($strQuery);

		} catch (PDOException $e)
		{
			echo $e->getMessage();
			echo "<br><br>Database -- NOT -- loaded successfully .. ";
			die( "<br><br>Query Closed !!! $error");
		}
	}	
} 
if ( isset($_POST["hvAccio"]))
{
	if ($_POST["hvAccio"] == "HoresVarModifica")
	{
		//Print " Modificar Hores Var... amb dades antigues ".$_POST["diahv"]." ".$_POST["obrehv"]." ".$_POST["tancahv"]."  ".$_POST["llochv"];
		//print " <br>";
		//print " Per Hores Noves ".$_POST["dia".$_POST["hvId"]]." ".$_POST["obre".$_POST["hvId"]]."  ".$_POST["tanca".$_POST["hvId"]]."  ".$_POST["lloc".$_POST["hvId"]];
		 try{
		$strQuery = "UPDATE HorarisVariables SET Dia = '".$_POST["dia".$_POST["hvId"]]."', obre='".$_POST["obre".$_POST["hvId"]]."',tanca='".$_POST["tanca".$_POST["hvId"]]."',lloc='".$_POST["lloc".$_POST["hvId"]]."'  where Dia = '".$_POST["diahv"]."' and obre ='".$_POST["obrehv"]."' and tanca ='".$_POST["tancahv"]."' and lloc ='".$_POST["llochv"]."'";
		$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
//		print $strQuery;
		$db->exec($strQuery);

		} catch (PDOException $e)
		{
			echo $e->getMessage();
			echo "<br><br>Database -- NOT -- loaded successfully .. ";
			die( "<br><br>Query Closed !!! $error");
		}
	}
	if ($_POST["hvAccio"] == "HoresVarElimina")
	{
		//Print " Esborrar Hores Variables .. amb dades antigues  ".$_POST["diahv"]." ".$_POST["obrehv"]." ".$_POST["tancahv"]."  ".$_POST["llochv"];
		 try{
		$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
		$strQuery = "DELETE FROM HorarisVariables where Dia='".$_POST["diahv"]."' and obre ='".$_POST["obrehv"]."' and tanca ='".$_POST["tancahv"]."' and lloc ='".$_POST["llochv"]."'";
//		print $strQuery;
		$db->exec($strQuery);

		} catch (PDOException $e)
		{
			echo $e->getMessage();
			echo "<br><br>Database -- NOT -- loaded successfully .. ";
			die( "<br><br>Query Closed !!! $error");
		}
	}	
} 
?>
<form name="horaris" action="horaris.php" method="post" enctype="multipart/form-data" id="horaris">
<div class="fonsMenuPpal" ><a href="#" onclick="javascript:Collapse('Afegirhoraris');" >Affegir nou horari</a></div>
<div id="Afegirhoraris" style="visibility:collapse;">
	<table class="taulaFormInterior">
		<tr>
			<td>Llocs:</td>
			<td>
				<select name="Lloc" class="input">
					<option value = ""></option>
					<option value="Telestany">Telestany</option>
					<option value="CCCornella">Centre Cultural Cornellà</option>
				</select>
			</td>
			<td><?if(isset($_POST["Lloc"])){
	if ( $_POST["Lloc"] != "") {
		print "Lloc triat";
	} else {
		print " No has triat cap lloc ! ";
	}
}
?>
			</td>
		</tr>
	</table>
<table class="taulaFormInterior">	
	<tr><td>Entra Horari EXtraordinari: </td><td><td>
				<? print CrearSelect("year2",2011,2015); ?> /
				<? print CrearSelect("month2",01,12); ?> /
				<? print CrearSelect("day2",01,31); ?> Horaentra;
				<? print CrearSelect("hour2",00,23); ?>:
				<? print CrearSelect("minute2",00,55); ?>  Horasurt;
				<? print CrearSelect("hour3",00,23); ?>:
				<? print CrearSelect("minute3",00,55); ?>

	<input type="button" value="Cal" class="inputBoto" onclick="displayCalendarSelectBox(document.forms[0].year2,document.forms[0].month2,document.forms[0].day2,document.forms[0].hour2,document.forms[0].minute2,this)">
	<input type="submit" value="Envia" name="Envia"  class="inputBoto" />
	</td>
	<td>&nbsp;&nbsp;
	</td>
	</tr></table>
	<table class="taulaFormInterior">
	<tr>
	<td>Dies Setmana
	</td>
	<td>
	<table ><tr><td>
	Dilluns</td><td><input type="checkbox" name="Dilluns" value="Dilluns" class="inputcheckbox"></td>
	<td>
	Dimarts</td><td><input type="checkbox" name="Dimarts" value="Dimarts" class="inputcheckbox"></td>
	<td>
	Dimecres</td><td><input type="checkbox" name="Dimecres" value="Dimecres" class="inputcheckbox"></td>
	</tr>
	<tr><td>
	Dijous</td><td><input type="checkbox" name="Dijous" value="Dijous" class="inputcheckbox"></td><td>
	Divendres</td><td><input type="checkbox" name="Divendres" value="Divendres" class="inputcheckbox"></td> <td>
	Dissabte</td><td><input type="checkbox" name="Dissabte" value="Dissabte" class="inputcheckbox"></td></tr>
<tr><td>	
	Diumenge</td><td><input type="checkbox" name="Diumenge" value="Diumenge" class="inputcheckbox"></td></tr>
	</table>
	</td>
	<td>Hora Entra:<td>
	<td><? print CrearSelect("hourEntra",00,23); ?>:
	<? print CrearSelect("minuteEntra",00,55); ?>
	</td>
	<td>Hora Surt:</td>
	<td><? print CrearSelect("hourSurt",00,23); ?>:
		<?print CrearSelect("minuteSurt",00,55); ?>
	</td>
	<td><input type="submit" value="Envia" name="HFix" class="inputBoto"></td>
	</tr>
	</td>
	</tr>	
	</table>
</div>	
	<br/>
	<br/>
	<table class="taulaFormInterior">
	<tr>
	<td class="titolTaula">Horaris Fix </td>
	</tr>
	<td><? 
	print "<input type='hidden' id='obreh' name='obreh' value ='' />";
	print "<input type='hidden' id='tancah' name='tancah' value ='' />";
	print "<input type='hidden' id='lloch' name='lloch' value ='' />";		
	print "<input type='hidden' id='diesh' name='diesh' value ='' />";	
	print "<input type='hidden' id='hfixAccio' name='hfixAccio' value ='' />";				
	print "<input type='hidden' id='hfixId' name='hfixId' value ='' />";
	try{
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
	//$db->exec($strQuery);
	$result = $db->query("select * from HorarisFix");
	$i = 0;
	print "<tr><td class='trColor1'>Hora Entra</td><td class='trColor1'>Hora Surt</td><td class='trColor1'>Lloc</td><td class='trColor1'>Dies</td><td></td><td></td></tr>";
	foreach($result as $row)
	{
	print "<tr>";
	print "<td><input type='text' name='obre".$i."' value ='".$row[0]."' class='input' /></td>";
	print "<td><input type='text' name='tanca".$i."' value ='".$row[1]."' class='input' /></td>";
	print "<td><input type='text' name='lloc".$i."' value ='".$row[2]."'  class='input'/></td>";	
	print "<td><input type='text' name='dies".$i."' value ='".$row[3]."' size='70' class='input'/></td>";	
	print "<td><a href=\"javascript:Accio('".$row[0]."','".$row[1]."','".$row[2]."','HoresFixElimina','".$row[3]."',".$i.");\"> Elimina|</a></td>";
	print "<td><a href=\"javascript:Accio('".$row[0]."','".$row[1]."','".$row[2]."','HoresFixModifica','".$row[3]."',".$i.");\"> Modifica</a></td>";
	print "</tr>";
	$i = $i+1;
	}
	
} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}	
	?></td>
	</table>
	<table class="taulaFormInterior">
	<tr>
	<td class="titolTaula">Horaris Extraordinaris</td>
	<td>
<? 
	print "<input type='hidden' id='diahv' name='diahv' value ='' />";
	print "<input type='hidden' id='obrehv' name='obrehv' value ='' />";
	print "<input type='hidden' id='tancahv' name='tancahv' value ='' />";
	print "<input type='hidden' id='llochv' name='llochv' value ='' />";		
	print "<input type='hidden' id='hvAccio' name='hvAccio' value ='' />";				
	print "<input type='hidden' id='hvId' name='hvId' value ='' />";
	try{
	$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
	//$db->exec($strQuery);
	$result = $db->query("select * from HorarisVariables");
	$i =0;
	foreach($result as $row)
	{
	print "<tr>";
	print "<td class='trColor1'>Dia</td>";
	print "<td class='trColor1'><input type='text' name='dia".$i."' value ='".$row[0]."'  class='input'/></td>";
	print "<td class='trColor1'>Obre</td>";
	print "<td class='trColor1'><input type='text' name='obre".$i."' value ='".$row[1]."'  class='input'/></td>";
	print "<td class='trColor1'>Tanca</td>";
	print "<td class='trColor1'><input type='text' name='tanca".$i."' value ='".$row[2]."' class='input' /></td>";
	print "<td class='trColor1'>Lloc</td>";
	print "<td class='trColor1'><input type='text' name='lloc".$i."' value ='".$row[3]."'  class='input'/></td>";	
	print "<td><a href=\"javascript:AccioV('".$row[0]."','".$row[1]."','".$row[2]."','".$row[3]."','HoresVarElimina',".$i.");\"> Elimina</a></td>";
	print "<td><a href=\"javascript:AccioV('".$row[0]."','".$row[1]."','".$row[2]."','".$row[3]."','HoresVarModifica',".$i.");\"> Modifica</a></td>";
	print "</tr>";
	$i = $i+1;
	}
	
} catch (PDOException $e)
{
   echo $e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}	
	?>
	<?
		function Select($nom,$valor)
		{
			if (isset($_POST[$nom]))
			{
				if ( $_POST[$nom] == $valor)
				{
					return print "selected";
				}
			}
		}
		function Crearselect($nom,$inici,$fi)
		{
		
		  $html = '<select name="'.$nom.'" class="input">';
		  for ($i = $inici; $i <= $fi; $i++)
		  {
			if ($i < 10) {
				$num = "0".$i;
			} else {
				$num = $i;
			}
			if ( isset($_POST[$nom]))
			{
				if ( $_POST[$nom] == $num )
				{
				$html .= '<option value="'.$num.'" selected>'.$num.'</option>';
				} else {
				$html .= '<option value="'.$num.'">'.$num.'</option>';
				}
			} else {
				$html .= '<option value="'.$num.'">'.$num.'</option>';
			}
		  }
		  $html .= '</select>';		
		return $html;
		}
	?>
	</td>
	</tr>
	</table>
	</form>