#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int roll_dice() {
    return rand() % 6 + 1;
}

char play_craps() {
    int point = 0;
    while (1) {
        int dice1 = roll_dice();
        int dice2 = roll_dice();
        int total = dice1 + dice2;

        if (point == 0) {
            if (total == 7 || total == 11)
                return 'p';
            else if (total == 2 || total == 3 || total == 12)
                return 'h';
            else
                point = total;
        } else {
            if (total == 7)
                return 'h';
            else if (total == point)
                return 'p';
        }
    }
}

void simulate_games(int num_games, int *player_wins, int *house_wins) {
    for (int i = 0; i < num_games; i++) {
        char result = play_craps();
        if (result == 'p')
            (*player_wins)++;
        else
            (*house_wins)++;
    }
}

void print_rules() {
    printf("Welcome to the casino game \"Craps\"!\n");
    printf("Rules:\n");
    printf("1. Player rolls two dice.\n");
    printf("2. If the sum is 7 or 11 on the first throw, the player wins.\n");
    printf("3. If the sum is 2, 3, or 12 on the first throw, the house wins.\n");
    printf("4. If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, that sum becomes the player's point.\n");
    printf("5. To win, the player must continue rolling the dice until they match the \"point\" or roll a 7.\n");
    printf("6. If the player rolls a 7 before matching the point, the house wins.\n");
}

int main() {
    srand(time(0));
    int num_games = 1000000;
    int player_wins = 0;
    int house_wins = 0;

    char play_game;
    printf("Do you want to play the game? (y/n): ");
    scanf(" %c", &play_game);

    if (play_game == 'y' || play_game == 'Y') {
        print_rules();
        simulate_games(num_games, &player_wins, &house_wins);

        printf("\nNumber of Games Won by the Player: %d\n", player_wins);
        printf("Number of Games Won by the House: %d\n", house_wins);
        printf("Percent Probability the Player Wins: %.2f%%\n", (float)player_wins / num_games * 100);
        printf("Percent Probability the House Wins: %.2f%%\n", (float)house_wins / num_games * 100);
    } else {
        printf("Maybe next time! Have a great day!\n");
    }

    return 0;
}
