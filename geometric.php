<?php
//amari grimes
//theory programming 
//this program takes the base program for geometric solving that we did in python and converts it to PHP

function rec() { //func for rectangle
    $b = (int) readline("please enter the base: ");
    $h = (int) readline("please enter the height: ");
    
    if ($b >= 0 && $h >= 0) { //checking for valid inputs and calculating
        $area = $b * $h;
        $per = 2 * ($b + $h);
    
        echo "the area of the rectangle is: $area\n";
        echo "the perimeter of the rectangle is: $per\n";
    } 
}

function circ() { //func for circle
    $r = (int) readline("please enter the radius: ");
    
    if ($r >= 0) { //checking for valid inputs and calculating
        $area = M_PI * pow($r, 2);
        $circumference = 2 * M_PI * $r;
    
        echo "the area of the circle is: $area\n";
        echo "the circumference of the circle is: $circumference\n";
    } 
}

function hex() { //func for hexagon
    $s = (int) readline("please enter the side: ");
    
    if ($s >= 0) { //checking for valid inputs and calculating
        $area = (3 * sqrt(3) * pow($s, 2)) / 2;
        $per = 6 * $s;
    
        echo "the area of the hexagon is: $area\n";
        echo "the perimeter of the hexagon is: $per\n";
    } 
}

function pent() { //func for pentagon
    $s = (int) readline("please enter the side: ");
    $a = (int) readline("please enter the apothem: ");
    
    if ($s >= 0 && $a >= 0) { //checking for valid inputs and calculating
        $per = 5 * $s;
        $area = 0.5 * $per * $a;
    
        echo "the area of the pentagon is: $area\n";
        echo "the perimeter of the pentagon is: $per\n";
    } 
}

function menu() { //func for menu
    while (true) {
        $user = (int) readline("please choose a shape: 
              1 - rectangle
              2 - circle 
              3 - hexagon 
              4 - pentagon
              5 - quit\n");

        if ($user == 1) {
            rec();
        } elseif ($user == 2) {
            circ();
        } elseif ($user == 3) {
            hex();
        } elseif ($user == 4) {
            pent();
        } elseif ($user == 5) {
            echo "goodbye!\n";
            break;
        } else { //checking for valid input 
            echo "invalid number, please try again.\n";
        }
    }
}

menu();

?>
