<?php
function api_call($url, $args){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_VERBOSE, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);     
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST,1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $args);
    $result = curl_exec($ch);
    return $result;
}

if (isset($_POST["view"])){
    $view = $_POST["view"];
    switch ($view) {
        case "login":
            $url = "http://127.0.0.1:8000/login";
            $args = array(
                "username" => $_POST["username"],
                "password" => $_POST["password"],
            );
            $result = api_call($url, $args);
            break;
        case "games":
            $url = "http://127.0.0.1:8000/games";
            $args = array();
            $result = api_call($url, $args);
            break;
        case "game":
            $url = "http://127.0.0.1:8000/game/".$_POST["name"];
            $args = array();
            $result = api_call($url, $args);
            break;
        case "player":
            $url = "http://127.0.0.1:8000/player/".$_POST["username"];
            $args = array();
            $result = api_call($url, $args);
            break;

    }
}
?>
<html>
<head>
<title>wordrobber server-side test page</title>
</head>
<body>
<?
if (isset($_POST["view"])){
?>
<h1>Result</h1>
URL:
<pre>
<?=$url?>
</pre>
POST:
<pre>
<?
print_r($args);
?>
</pre>
Return:
<pre>
<?=$result?>
</pre>
<?}?>

<hr/>
<h1>Login</h1>
<form action="test.php" method="post">
<input name="view" type="hidden" value="login" />
username
<input name="username" type="text" />
<br/>
password
<input name="password" type="password" />
<br/>
<input type="submit" />
</form>

<hr/>
<h1>Games</h1>
<form action="test.php" method="post">
<input name="view" type="hidden" value="games" />
<input type="submit" />
</form>

<hr/>
<h1>Game</h1>
<form action="test.php" method="post">
<input name="view" type="hidden" value="game" />
name
<input name="name" type="text" />
<br/>
<input type="submit" />
</form>

<hr/>
<h1>Player</h1>
<form action="test.php" method="post">
<input name="view" type="hidden" value="player" />
username
<input name="username" type="text" />
<br/>
<input type="submit" />
</form>

</body>
</html>
