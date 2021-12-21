<?php

$file = file_get_contents("/tmp/palabras_del_dia.json");

header('Content-type:application/json;charset=utf-8');
echo $file;