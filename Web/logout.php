<?php
include("func.php");
logout();
if(!isLoggedIn())
{
    header('Location: login_form.php');
    die();
}
?>