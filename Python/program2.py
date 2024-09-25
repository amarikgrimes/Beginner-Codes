import math

def rec()
    b = int(input("please enter the base:"))
    h = int(input("please enter the height:"))
    
    if b >= 0 and h >= 0:
        area = b*h 
        per = (2*b)+(2*h)
    
    print("the area is:", area)
    print("the perimeter is:" per)
def circ()
    r = int(input("please enter the radius:"))
    
    if r >= 0:
        area = (math.pi) * r**2
        circumference = 2 * r * (math.pi)
    
    print("the area is:", area)
    print("the perimeter is:" circumference)
def hex()
    s = int(input("please enter the side:"))
    
    if s >= 0:
        area = (3 * math.sqrt(3*s**2))/2
        per = 6*s
    
    print("the area is:", area)
    print("the perimeter is:" per)
def pent()
    s = int(input("please enter the side:"))
    a = int(input("please enter the apothem:"))

    if s >= 0:
        area = 1/2 * per * a
        per = 5*s
    
    print("the area is:", area)
    print("the perimeter is:" per)


def menu()
   user = int(input("""Please choose a shape: 
              1 - rectangle
              2 - circle 
              3 - hexagon 
              4 - pentagon
              5 - quit """))
    if user == 1:
        rec()
    if user == 2:
       circ()
    if user == 3: 
       hex()
    if user == 4:
       pent()
    if user == 5:
       quit
