#prompt the user to enter number of days rented, start odometer and end odometer
days = int(input("Enter number of days rented:"))
start = int(input("Enter the odometer at the start of the rental:"))
end = int(input("Enter the odometer at the end of the rental:"))
#define the base, miles, milage and total variable (calculate the math)
base = 40.99 * days
miles = end - start
mileage = (end - start)*.25
total = base + mileage 
#print days rented, miles drove and amount charged
print("You rented the vehicle for",days,"day(s)")
print("You drove", miles, "miles during the rental period")
print("Your total amount due is:$",round(total,2))
