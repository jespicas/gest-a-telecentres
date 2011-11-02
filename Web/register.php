<?php
//retrieve our data from POST
$username = $_POST['username'];
$pass1 = $_POST['pass1'];
$pass2 = $_POST['pass2'];
if($pass1 != $pass2)
    header('Location: register_form.php');
if(strlen($username) > 30)
    header('Location: register_form.php');
$hash = hash('sha256', $pass1);
function createSalt()
{
    $string = md5(uniqid(rand(), true));
    return substr($string, 0, 3);
}
$salt = createSalt();
$hash = hash('sha256', $salt . $hash);

try{
$db=new PDO("sqlite:/usr/share/local/telestany/telestany.sqlite");
$result = $db->query("INSERT INTO usersWeb ( username, password, salt ) VALUES ( '$username' , '$hash' , '$salt' );");
if ($result === FALSE)
    {
        print_r($db->errorInfo());
        die();
    }

} catch (PDOException $e)
{
   echo $e->getcode().':'.$e->getMessage();
    echo "<br><br>Database -- NOT -- loaded successfully .. ";
    die( "<br><br>Query Closed !!! $error");
}
header('Location: login_form.php');	
?>