totalmiles = 0
totalgallons = 0
list = []

while True:
  gallons = float(input("Enter the gallons used(-1 to end):"))
  if gallons == -1:
    break
  miles = int(input("Enter miles driven:"))
  list.append(miles)  
  totalmiles += miles
  totalgallons += gallons
  
mpg = totalmiles / totalgallons

print("You drove the following distances:", list )
print("Your overall average miles per gallon is: ", mpg)
