<?php

$f = "./palabras_del_dia.json";

$file = file_get_contents($f);

header('Access-Control-Allow-Origin: *');
header('Content-type:application/json;charset=utf-8');
echo $file;
