#import the random number module
import random

#create a menu function for the user to look at and choose from
def menu():
  print("Welcome to Dr.G's Roulette Table!")
  print("Game Rules:")
  print("  Every bet costs $5")
  print("Betting Options:")
  print(
      """  1. Straight Up: Single number selection. Potential payout is 35 to 1. 
  2. Split: Single number selection. Covers the chosen number and one adjacent number (above or below). Potential payout is 17 to 1.
  3. Street: Single number selection. Covers the chosen number and the next two numbers in sequence. Potential payout is 11 to 1.
  4. Top: Any number from 1-18. Potential payout is even money ($10).
  5. Bottom: Any number from 19-36. Potential payout is even money ($10).
  6. Even/Odd: Covers all even or all odd numbers from 1-36. Potential payout is even money ($10).
  7. Quit Game""")
#call the menu function
menu()
print("\n")
#establish counter variables for the betting such as bet and rounds
bet = 5
round = 1
#begin the while loop by asking the user for their bet choice
while True:
  #print the round number
  print("Round", round, ":")
  betchoice = int(input("Your choice (Enter a number 1 to 7):"))
  #establish sentinel value
  if betchoice == 7:
    print( "Thank you for playing Dr.G's Roulette Table! We hope to see you again soon!")
    break
#begin writing the generating/caluclating for each bet choie
  elif betchoice == 1:
#ask the user for which number they would like to bet on in straight up
    number = int(input("Which number would you like to select for Straight up (1-36)?:"))
#spin the wheel to show what the code is doing with their stored number
    print("......Spinning the Wheel........")
    #call the random number imported module
    betran = random.randint(1, 36)
    #only using this print statment to check if the code is working
    print("The rolled number is:",betran)
    #make if statements for what happens to the bet money when the bet conditions are met
    if number == betran:
      roundtotal = 35 * bet
      print("Congratulations! You win:$",roundtotal)
    #if statement for when they are not met
    if number != betran:
      print("Sorry, you lose this round. Better luck next time!")
    #add as a round counter at the end of every choice
    round += 1
    print("\n")
#repeat the same steps from betchoice #1 with #2
  elif betchoice == 2:
    number = int(input("Which number would you like to select for Split (1-36)?:"))
    print("......Spinning the Wheel........")
    betran = random.randint(1, 36)
    print("The rolled number is:",betran)
#create an if statament that checks if the number inputed is equal to, +1 or -1 of betran
    if betran == number or betran == number + 1 or betran == number - 1:
      roundtotal = 17 * bet 
      print("Congratulations! You win:$",roundtotal)
    else:
      print("Sorry, you lose this round. Better luck next time!")
    round += 1
    print("\n")
#repeat the same steps from betchoice #2 with #3
  elif betchoice == 3:
    number = int(input("Which number would you like to select for Street (1-36)?:"))
    print("......Spinning the Wheel........")
    betran = random.randint(1, 36)
    print("The rolled number is:",betran)
#create an if statemanet that checks if the randomized betran is number + 1 or +2
    if betran == number or betran == number + 1 or betran == number + 2:
      roundtotal = 11 * bet
      print("Congratulations! You win:$",roundtotal)
    else:
      print("Sorry, you lose this round. Better luck next time!")
    round += 1
    print("\n")
#create a betchoice for 4 that check whether the random number is 1-18 inclusive
  elif betchoice == 4:
    print("......Spinning the Wheel........")
    betran = random.randint(1,36)
    print("The rolled number is:",betran)
    if betran >= 1 and betran <= 18:
      roundtotal = 10
      print("Congratulations! You win:$",roundtotal)
    else:
      print("Sorry, you lose this round. Better luck next time!")
    round += 1
    print("\n")
#repeat the same steps from betchoice 4 except check if the random number is 19-36
  elif betchoice == 5:
    print("......Spinning the Wheel........")
    betran = random.randint(1,36)
    print("The rolled number is:",betran)
    if betran >= 19 and betran <= 36:
      roundtotal = 10 
      print("Congratulations! You win:$",roundtotal)
    else:
      print("Sorry, you lose this round. Better luck next time!")
    round += 1
    print("\n")
#start another if statement for betchoice 6 because its structure is different than 1,2,3
  elif betchoice == 6:
    choice = (input("Your Preference for Even/Odd:"))
    print("......Spinning the Wheel........")
    betran = random.randint(1, 36)
    print("The rolled number is:",betran)
    #create if statments that checks if betran is even or odd
    if betran % 2 == 0:
      betran = 'Even'
    elif betran % 2 != 0:
      betran = 'Odd'
#create an if statment that checks if betran eqauls the user choice
    if choice == betran:
      roundtotal = 10
      print("Congratulations! You win:$",roundtotal)
    else:
      print("Sorry, you lose this round. Better luck next time!")
    round += 1
    print("\n")

#
