<?php
#amari grimes
#theory programming
#program that creates a list of 32 random numbers, calculates the sum, the average, the lowest and highest numbers in the list and sorted in order using the C++ program as a base



#function for creating list and calculating 
function create(){
    $SIZE = 32;
    $ran = array();

    #generating random numbers during this time
    srand(time());

    #creating the random list of numbers 
    echo"list 32 random numbers: \n";
    for ($i = 0; $i < $SIZE; $i++){
        $ran[$i] = rand(0, 100);
        echo $ran[$i] . " ";
    }
    echo "\n";

    #calculate sum 
    $sum = array_sum($ran);
    echo "sum of the numbers:" . $sum . "\n";

    #calculate average 
    $averg = $sum / $SIZE;
    echo "average of the numbers:". $averg . "\n";

    #smallest and largest number calc 
    $small = min($ran);
    $large = max($ran);
    echo "smallest number: " . $small . "\n" . "largest number:" . $large . "\n";

    #sorting 
    sort($ran);
    echo "sorted list of numbers:";
    foreach($ran as $num){
        echo $num . " ";
    }
    echo "\n";
}
create();

?>