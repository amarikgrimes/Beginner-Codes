#amari grimes
#theory programming
#this is a python pet class example that was done in and out of class to show how you store an objects attributes and access the private information with the get method. 


#creating the pet class
class pet:
    
    #initializer method
    def __init__(self, name = "", animal_type = "", age = 0) :
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
        #creatng the mutator methods
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age 
    
    #creating the get or retrieving method
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
        

def main():
    #empty space for pet input
    mypet = pet()

    #create a place for the user to input the variables 
    name = input("enter the name of your pet:")
    animal_type = input("enter the type of animal:")
    age = int(input("enter the age of your pet:"))

    #set the user input and empty pet variable to the created mutators 
    mypet.set_name(name)
    mypet.set_animal_type(animal_type)
    mypet.set_age(age)

    #use the get methods to print the classes 
    print("your pet information:")
    print("name:", mypet.get_name())
    print("animal type:", mypet.get_animal_type())
    print("age:", mypet.get_age())

if __name__ == "__main__":
    main()
