#ask the user for the nuber of lattes, expressos and cappuccinos
lattes = int(input("How many lattes did you order?: "))
capps = int(input("How many cappuccinos did you order?: "))
express = int(input("How many expressos did you order?: "))
#calculate price for lattes, expressos and cappucinos
latprice = float(lattes * 3.50)
capprice = float(capps * 4.00)
expprice = float(express * 2.50)
#calculate total overall price
total = (latprice + capprice + expprice)
#print ending price for all variables 
print("\n")
print("Total cost for lattes: $",latprice)
print("Total cost for cappucinos: $",capprice)
print("Total cost for expressos: $",expprice)
print("Your total bill is: $",total)
