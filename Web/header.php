<?
session_start();
include("func.php");
//if the user has not logged in

if(!isLoggedIn())
{
    header('Location: login_form.php');
    die();
}
?>
