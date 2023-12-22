#define counter for total odd, even and zeros
totalodd = 0
totaleven = 0
totalzeros = 0
#start while loop and ask for user input
while True:
  value = int(input("Please enter a value(-99 to quit): "))
  #add an if statement in order to determine the sentinel
  if value == -99:
     break
    #add two elif statments in order to determine if the value is an even or zero
  elif value == 0:
    #add to its respective counter variable
    totalzeros += 1
  elif value %2 == 0:
    #add to its respective counter variable
    totaleven += 1
    #add an else statement in order to determine if the value is an odd value
  else:
    #add to its respective counter variable
    totalodd += 1
#print the totaleven, totalodd and totalzeros 
print(totaleven, "even")
print(totalodd, "odd")
print(totalzeros, "zeros were entered")