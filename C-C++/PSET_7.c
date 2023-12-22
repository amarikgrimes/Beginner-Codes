#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int guess, number, count;
    char playAgain;

    srand(time(0)); // Seed the random number generator

    do {
        printf("\n******** BEGIN a GAME ********\n");
        number = rand() % 100 + 1; // Generate a random number between 1 and 100
        count = 0;

        printf("I'm thinking of a number. Can you guess what it is? ");
        do {
            scanf("%d", &guess);
            count++;

            if (guess > number)
                printf("Sorry, that's too high.\nGuess again: ");
            else if (guess < number)
                printf("No, that's too low.\nGuess again: ");
            else
                printf("Congratulations! You guessed it!\n"
                       "I was thinking of the number %d.\n"
                       "You got it right in %d guesses.\n", number, count);

        } while (guess != number);

        printf("\n******** END OF a GAME ********\n");
        printf("Would you like to play another game? ('y' or 'n'): ");
        scanf(" %c", &playAgain);

    } while (playAgain == 'y');

    return 0;
}
