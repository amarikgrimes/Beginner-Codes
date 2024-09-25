import math
import cmath

for i in range (4):
    a = int(input("please enter a:"))
    b = int(input("please enter b:"))
    c = int(input("please enter c:"))

    if a == 0:
        print("A coefficent can not be 0, please try again!")
    else:
        dis = (b**2 - 4*a*c)

        if dis > 0:
            root1 = (-b + math.sqrt(dis)) /(2*a)
            root2 = (-b - math.sqrt(dis)) /(2*a)
            print("The equation has two distinct roots:", root1, root2)
        if dis == 0:
            root1 = -b / (2*a)
            print("The equation has one distinct root:", root1)
        if dis < 0:
            root1 = (-b + cmath.sqrt(dis))/(2*a)
            root2 = (-b - cmath.sqrt(dis))/(2*a)
            print("The equation has two complex roots:", root1, root2)