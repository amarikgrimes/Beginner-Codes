#Amari Grimes
#Tortoise and Hare Simulation Project
#CIS 111 - 04
#November 22nd, 2023

#import the random integer module
import random
#import time module
import time
#define the tortoisemovement
def tortmove():
  toran = random.randint(1, 10)
#if the random generated number for the tortoise is greater than 1 but less then five then it is a fast pod movement and the tortoise is moving quickly 
  if 1 <= toran <= 5:
   print("The tortoise is moving quickly! Watch out hare!\n")
   return "Fast pod"
#if the random generated number for the tortoise is greater than 6 but less than 7 the tortoise is slipping and not moving as quickly. The tortoise is moving 6 sqaures to the left
  elif 6 <= toran <= 7:  
   print("The tortoise is catching their breath for a moment.\n")
   return "Slip"
#if the random generated number is anything other than those two movements than the tortoise is moving at its normal speed
  else:
    print("The tortoise is moving slowley but surely!\n")
    return "Slow pod"
#create a function for the hares movement
def haremove():
  hran = random.randint(1, 10)
  #if the random generated number is greater than or equal to one and less than or equal to two then the hare is sleeping
  if 1 <= hran <= 2:
    print("The hare has fallen asleep!\n")
    pass
  #if the random generated number is greater than or equal to three and less than or equal to 4 then the hare is moving quickly
  elif 3 <= hran <= 4:
    print("The hare has caught a second wind!\n")
    return "Big hop"
  #if the random generated number eqauls 5 then the hare is slwoing down
  elif hran == 5:
    print("The hare has taken a tumble!\n")
    return "Big slip"
  #if the random generated number is greater than or equal to 6 and less than or equal to 8 then the hare did a small hop
  elif 6 <= hran <= 8:
    print("The hare is taking this race one small hop at a time. \n")
    return "Small hop"
  #if the random generated number is anything else, the hare is falling behind just a bit
  else: 
    print("The hare has slipped and is letting the tortoise catch up !\n")
#define race function    
def race():
#define a counter for the tortoises position and the hares position
  tortpos = 1
  harepos = 1
#create a variable to calculate start time
  start_time = time.time()
#print statments to initialize the beginning of the race
  print("Ready...")
  print("Set...")
  print("BANG !!!!!")
  print("AND THEY’RE OFF !!!!!\n")
#this while loop is here to make sure that the race stops when one of the animals reaches square 70
  while tortpos < 70 and harepos < 70:
    #count the time that has gone by in the interval of 1 sec
    time.sleep(1) 
    #create a variable to count the time of every round
    elapsed_time = round(time.time() - start_time, 2)
    #create variables for the animal movements in the race
    tortrace = tortmove()
    harerace = haremove()
    #fix positions if there is a slip before sqaure 1 then the animals must move back or simply stay at sqaure one
    if tortpos < 1:
      tortpos = 1
    elif harepos < 1:
      harepos = 1
  #define all of the positions and how many squares to move and which way it will be moving 
    if tortrace == "Fast pod":
      tortpos += 3
      print("Tortoise Position:",tortpos)
    elif tortrace == "Slip":
      if tortpos >= 6: 
        tortpos -= 6 
      else:
        tortpos = 1
      print("Tortoise Position:",tortpos)
    else:
      tortpos += 1
      print("Tortoise Position:",tortpos)
    if harerace == "Sleep":
      harepos += 0
      print("Hare Position:",harepos,"\n")
    elif harerace == "Big hop":
      harepos += 9
      print("Hare Position:",harepos,"\n")
    elif harerace == "Big slip":
      if harepos >= 12:
        harepos -= 12  
      else:
        harepos = 1
      print("Hare Position:",harepos,"\n")
    elif harerace == "Small hop":
      harepos += 1
      print("Hare Position:",harepos,"\n")
    else:
      if harepos >= 2:
        harepos -= 2
      else:
        harepos = 1
      print("Hare Position:",harepos,"\n")
#account for if both the hare and tortoise are on the same square
    if tortpos == harepos:
        print("OUCH!!!\n")
        print("Hare Position:",harepos,"\n")
#create if statements for reading and printing who won the race
    #if both animals end on the 70 space together it is a tie
    elif tortpos >= 70 and harepos >= 70:
        print("It's a tie. Tortoise won in our hearts!")
        break
      #if the tortoise ends on 70 it wins
    elif tortpos >= 70:
        print("TORTOISE WINS!!! YAYY!!")
        break
    #if the hare ends on 70 it wins
    elif harepos >= 70:
        print("Hare wins! Yuch.")
        break
     #display elapsed time after each tick
    print("Elapsed Time:", elapsed_time, "seconds\n")  
race()
