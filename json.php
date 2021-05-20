<?php

$j = json_decode(file_get_contents("/root/tools/result.json"), true);
echo $j[0];
echo $j[1];
echo $j[2];
