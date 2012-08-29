<?php
# read configuration file
$config = parse_ini_file(dirname(__FILE__) . "/config/config.ini");
?>
<html>
<head>
<title>Wordrobber</title>
<script type="text/javascript" src="jquery.js"></script> 
<script type="text/javascript">
/* jQuery functions for the Web Application interface */
$(document).ready(function(){
    /* click on "login" button sende username and password
     * and retrieve a session ID and a timestamp
     */
    $("#login").click(function(){
        $.ajax ({
            type: "POST",
            url: 'wsproxy.php',
            dataType: 'json',
            async: false,
            data: {
                /* the trailing slash is IMPORTANT for Django */
                url: 'http://<?=$config["webservice_url"]?>:<?=$config["webservice_port"]?>/login/',
                username: $("#username").val(),
                password: $("#password").val()
            },
            success: function (json) {
                window.alert("session ID: "+json.sessionid+"\ntimestamp: "+json.timestamp);
            }
        })   
    });
});
</script> 
</head>
<body>
