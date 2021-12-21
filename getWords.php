<?php

<<<<<<< HEAD
$f = "/tmp/palabras_del_dia.json";
=======
$f = "./palabras_del_dia.json";
>>>>>>> a0ad17e0ae5230cd26e0cbd90f26a8ab29cdb5cc

$file = file_get_contents($f);

header('Content-type:application/json;charset=utf-8');
echo $file;
