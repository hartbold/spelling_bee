<?php

$f = "/tmp/palabras_del_dia.json";

if(file_exists($f)){
    $file = file_get_contents($f);
} else {
    $file = '{
        "error": '.getcwd().'
      }';
}


header('Content-type:application/json;charset=utf-8');
echo $file;