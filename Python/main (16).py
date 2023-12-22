#name: amari grimes
#date: 02/17/2023
#course number:SCIS105
#section: 1
#title: number guesser
#program description: project that creates a guessing game for the user

import random
print("hi! welcome to the guessing game! please guess a number between 1-100 :) ")
print("\n")
guess = int(input("what is your guess?:" ))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
  if guess < correct_number :
    print("you got this! guess higher!")
    print("\n")
  if guess > correct_number :
    print("try guessing lower!")
    print("\n")
  guess_count += 1
  guess = int(input("what is your guess?:"))
print("\n")
print(f"congrats! the right answer is {correct_number}. It took you {guess_count} guesses. ")
