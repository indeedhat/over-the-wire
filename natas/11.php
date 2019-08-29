<?php

$data = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D');
$raw = json_encode(["showpassword"=>"no", "bgcolor"=>"#ffffff"]);

$key = '';
for ($i = 0; $i < strlen($data); $i++) {
    $key .= $data[$i] ^ $raw[$i % strlen($raw)];
}

print $key . PHP_EOL;

function xor_encrypt($in)
{
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for ($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


$d = ['bgcolor' => '#ffffff', 'showpassword' => 'yes'];
print base64_encode(xor_encrypt(json_encode($d)));
