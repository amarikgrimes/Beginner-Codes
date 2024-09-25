<?php
//amari grimes
//theory programming
//this program will take in the name and birth year of the user and output their name and age

// name and birth year
$name = readline("please enter your name: ");
$yearOfBirth = readline("please enter your birth year: ");

// current age and year calculations
$currentYear = date("Y");
$age = $currentYear - $yearOfBirth;

// dsplay message
echo "hello, $name ! you are $age years old.\n";
?>