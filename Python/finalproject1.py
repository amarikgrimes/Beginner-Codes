#name: amari grimes
#date: 2/23/2022
#course: SCIS105
#section: 1
#title: Final Programming Project
#description: creating a program where users choose from a menu of recipes and groccery lists

"""
1. create 6 comments for my name, date, course, section, title and description using hashtags
2. define the variables of original recipe, algorithmic recipe and adapted recipe as strings in three quotations on each side of the recipe texts 
3. define the variables of original groccery list, algorithmic groccery list and adapted groccery list as strings in three quotations on each side of the recipe texts
4. define a userinput asking which recipe the user would like to see
5. generate an if then statement that prints the original recipe when the user inputs the number 1 
6. define another userinput that asks whether the user would like to see the groccery list tied to that specific recipe 
7. create an if else statement that prints the groccery list if the user says yes and an "are you sure?" statement if the user inputs no 
8. repeat steps 5-7 for the algorithmic recipe and the adapted recipe having the user input 2 for algorthmic recipe and 3 for the adapted recipe
"""

original_recipe = """
1. Cook pasta in chicken stock until it still has a little bite to it (about 7-8 minutes). The pasta will continue to cook once it is placed in the oven to bake. 

2. Drain the pasta and add one stick of butter and stir (don’t stir too much - just enough for the butter to melt) 

3. Add 3/4 cup of sour cream to the pasta and stir

4. Add seasonings to taste (a little salt, pepper, garlic powder, onion powder, paprika) 

5. Add cheese (about 1 cup each) and stir 

6. In a bowl whisk eggs, milk and cream to make the custard 

7. Butter the bottom and sides of the baking pan

8. Add macaroni to the baking pan then continue to layer all ingredients until done (pasta, a cup and a half cheese, and about a cup of custard at a time)  

9. Top with a final layer of cheese and paprika  

10. Bake uncovered at 350° for 45 minutes to an hour

11. Let sit for 10 minutes before serving 
"""
algorithmic_recipe = """
1. Cook pasta in chicken stock for 7-8 minutes (The pasta will continue to cook once it is placed in the oven to bake) 

2. Drain the pasta 

3. Add one stick of butter 

4. Stir until butter is melted into pasta

5. Add 3/4 cup of sour cream to the pasta 

6. Stir until sour cream is fully combined

7. Add all seasonings

8. Add 1 cup of each cheese

9. Stir cheeses to melt

10. In a large bowl whisk eggs, milk, and cream to make the custard 

11. Butter the bottom and sides of the 11 x 17-inch baking pan

12. Add macaroni to the baking pan 

13. Add a cup of any cheese

14. Add a cup of Custard 

15. Repeat steps 12-15b until macaroni, cheese, and custard have been used up

16. Top with a final layer of cheese and paprika  

17. Bake uncovered at 350° for  1 hour

18. Let sit for 10 minutes before serving 
"""
adapted_recipe = """
1. Heat up a non stick skillet on medium heat

2. Once skillet heats up add in shrimp and cook for 2 minutes on both sides

3. Add in lobster and cook both until pink

4. Take skillet off the heat and set seafood aside

5. Cook pasta in chicken stock for 7-8 minutes (The pasta will continue to cook once it is placed in the oven to bake) 

6. Drain the pasta 

7. Add one stick of butter 

8. Stir until butter is melted into pasta

9. Add 3/4 cup of sour cream to the pasta 

10. Stir until sour cream is fully combined

11. Add all seasonings

12. Add 1 cup of each cheese

13. Stir cheeses to melt

14. In a large bowl whisk eggs, milk, and cream to make the custard 

15. Butter the bottom and sides of the 11 x 17-inch baking pan

16. Add macaroni to the baking pan 

17. Add a cup of any cheese

18. Add a cup of Custard 

19. Add some crab, lobster and shrimp

20. Repeat steps 12-15b until macaroni, cheese, and custard have been used up

21. Top with a final layer of cheese and paprika  

22. Bake uncovered at 350° for  1 hour

23. Let sit for 10 minutes before serving 
"""
original_groccery = """
Chicken stock 

Elbow pasta  

Cheese of choice 

Whole milk 

Heavy cream 

Eggs 

Sour cream 

Seasonings such as paprika, salt , pepper ( taste as you mix and adjust the seasonings! ) 

Butter
"""
algorithmic_groccery = """
Chicken stock 

Elbow pasta  

Mozzarella 

Sharp cheddar

Monetary jack 

Whole milk 

Heavy cream 

Eggs 

Sour cream 

Paprika

Salt 

Pepper

Garlic powder

Onion powder

Butter 

11 x 17 inch pan 
"""
adapted_groccery = """
Chicken stock 

Elbow pasta  

Shrimp

Lobster 

Crab meat

Mozzarella 

Sharp cheddar

Monetary jack 

Whole milk 

Heavy cream 

Eggs 

Sour cream 

Paprika

Salt 

Pepper

Garlic powder

Onion powder

Old bay

Butter 

11 x 17 inch pan 
"""
              
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*")
print("         Welcome to Mom's Cheesy Goodness Recipe!")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*")
print("\n")
print("PLEASE SELECT FROM THE FOLLOWING MENU:")
print("\n")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*")
print("1 - Original Recipe\n2 - Algorithmic Recipe\n3 - Adaptated Recipe  ")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*")
print("\n")
userinput = int(input("Which recipe would you like to see?: "))

if userinput == 1:
  print("\n")
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print(f"{original_recipe}") 
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print("\n")
  user_input= input("Would you like to see the groccery list for this recipe? Yes or No?: ")
  print("\n")
  if user_input == "yes": 
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("            Groccery list")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"{original_groccery}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Happy cooking!")
  else:
    user_input= input("Oh! are you sure?...: ")
    if user_input == "yes":
      print("\n")
      print("...Alright, have fun cooking!")
    else: 
      print("\n")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print(f"Okay here is the groccery list!\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n  {original_groccery}  ")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print("Happy cooking!")
if userinput == 2:
  print("\n")
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print(f"{algorithmic_recipe}") 
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print("\n")
  user_input= input("Would you like to see the groccery list for this recipe? Yes or No?: ")
  print("\n")
  if user_input == "yes":
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("            Groccery list")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"{algorithmic_groccery}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\n")
    print("Happy cooking!")
  else:
    user_input= input("Oh! are you sure?...: ")
    if user_input == "yes":
      print("\n")
      print("...Alright, have fun cooking!")
    else:
      print("\n")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print(f"Okay here is the groccery list!\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n  {algorithmic_groccery}  ")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print("Happy cooking!")

if userinput == 3:
  print("\n")
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print(f"{adapted_recipe}") 
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print("\n")
  user_input= input("Would you like to see the groccery list for this recipe? Yes or No?: ")
  print("\n")
  if user_input == "yes": 
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("            Groccery list")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"{adapted_groccery}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Happy cooking!")
  else:
    user_input= input("Oh! are you sure?...: ")
    if user_input == "yes":
      print("\n")
      print("...Alright, have fun cooking!")
    else: 
      print("\n")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print(f"Okay here is the groccery list!\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n  {adapted_groccery}  ")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print("Happy cooking!")
    
      
