#amari grimes
#theory program 
#guessing game that loops to allow 10 attempts and gives hints about guessing lower or higher after every guess

import random

def guessing():
    number = random.randint(1,101)
    count = 0

    while count < 10:
        guess = int(input("pick a number between 1-100: "))
        if guess > number:
            print("That guess is too high, pls try agan!")
            count += 1
        if guess < number:
            print("That guess is too low, please try again!")
            count += 1
        if guess == number: 
            print("Great job! You've guess correctly! The number was", number)
            break
        if count == 10:
            print("You've guessed too many times! The correct number was", number)
            break
guessing()
