<?php
function isLoggedIn()
{
    if(isset($_SESSION['valid']) && $_SESSION['valid'])
        return true;
    return false;
}
function logout()
{
    $_SESSION = array(); //destroy all of the session variables
    session_destroy();
}
?>
