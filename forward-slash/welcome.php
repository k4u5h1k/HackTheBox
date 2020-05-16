<?php
// Initialize the session
session_start();

// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    echo "Redirecting you to the login page";
    header("location: login.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <link rel="stylesheet" href="bootstrap.css">
    <style type="text/css">
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
    <div class="page-header">
        <h1>Hi, <b><?php echo htmlspecialchars($_SESSION["username"]); ?></b>. Welcome to your dashboard.</h1>
    </div>
    <p>

        <a href="reset-password.php" class="btn btn-warning">Reset Your Password</a>
        <a href="logout.php" class="btn btn-warning">Sign Out of Your Account</a><br><br>
        <a href="updusername.php" class="btn btn-warning">Change Your Username</a>
        <a href="profilepicture.php" class="btn btn-warning">Change Your Profile Picture</a> <br><br>
	<a href="environment.php" class="btn btn-warning">Quick Message</a>
	<a href="hof.php" class="btn btn-warning">Hall Of Fame</a>
    </p>
</body>
</html>
