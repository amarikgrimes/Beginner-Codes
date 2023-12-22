#name: amari grimes
#date: 2/6/2022
#course: SCIS105
#section: 1
#title: fortune cookie
#description: project that displays a random fortune cookie

import random

fortune_number = random.randint(1,3)
lucky_number = random.randint(1,100)

fortune_text = ""

if fortune_number == 1:
  fortune_text = ("today will be a walk in the park!")
if fortune_number == 2:
  fortune_text = ("today will be tough... but i know you'll get through it!")
if fortune_number == 3:
  fortune_text = ("you will find the love of your life this month!")
  

print(f"{fortune_text} your lucky number is: {lucky_number}")