<?php
/* wsproxy.php
 * This script works as a server-side proxy to access cross-domain
 * web services. The URL must be passed as an explicit parameter.
 * The whole POST is passed to the webservice; this is inefficient and
 * should be replaced by a more specialized proxy.
 */
$url = $_POST["url"];

$ch = curl_init();
curl_setopt($ch, CURLOPT_VERBOSE, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);     
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST,1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $_POST);

$result = curl_exec($ch);
curl_close($ch);

echo ($result);
?>
