#amari grimes
#theory programming
#this program does the quadratic equation base program that we did in python except it uses php as its language and is modified for that. 
<?php
// function for solving the quadratic
function solveQuadratic($a, $b, $c) {
    // calculating the discriminant: D = B^2 - 4AC
    $dis = ($b * $b) - (4 * $a * $c);

    // checking if the discrminent result gives two real roots
    if ($dis > 0) {
        $root1 = (-$b + sqrt($dis)) / (2 * $a);
        $root2 = (-$b - sqrt($dis)) / (2 * $a);
        echo "two distinct real roots: $root1 and $root2\n";
    } 
    // checking if the discriminant is 0 giving on real root
    elseif ($dis == 0) {
        $root = -$b / (2 * $a);
        echo "one real root: $root\n";
    } 
    // checking if the discriminant is less than 0 giving complex roots
    else {
        $realPart = -$b / (2 * $a);
        $imaginaryPart = sqrt(abs($dis)) / (2 * $a);
        echo "complex roots: $realPart + {$imaginaryPart}i and $realPart - {$imaginaryPart}i\n";
    }
}

// loop in order to solve 5 times
for ($i = 0; $i < 5; $i++) {
    // user input
    echo "enter A: ";
    $a = floatval(trim(fgets(STDIN)));
    
    echo "enter B: ";
    $b = floatval(trim(fgets(STDIN)));
    
    echo "enter C: ";
    $c = floatval(trim(fgets(STDIN)));

    // checking if a is not 0 so it is known that it is a proper equation
    if ($a == 0) {
        echo "coefficient A cannot be zero. this is not a quadratic equation.\n";
    } else {
        // solve the quadratic equation
        solveQuadratic($a, $b, $c);
    }

    echo "----------\n";  // separator between each iteration
}

?>