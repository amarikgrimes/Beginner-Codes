# amari grimes
# theory programming
# this program will create an animal inheritance test in Python 

# mammal class represents a generic mammal
class mammal:
    # __init__ method accepts arguments for the mammal's species and name
    def __init__(self, species, name):
        self._species = species
        self._name = name

    # show_species method displays a message indicating the mammal's species
    def show_species(self):
        print(f"I am a {self._species}")

    # make_sound method is the mammal's way of making a generic sound
    def make_sound(self):
        print("Grrrrr!")

    # action method is the mammal's way of doing a generic action
    def action(self):
        print("Walk!")

    # __str__ method returns information about the mammal
    def __str__(self):
        return f"Species: {self._species}, Name: {self._name}"

# frog class is a subclass of the Mammal class
class frog(mammal):
    def __init__(self, name):
        super().__init__('frog', name)
    
    def make_sound(self):
        print("ribbit!")

    def action(self):
        print("frolick in the grass")

    def __str__(self):
        return f"{self._name} is a water-loving animal, known for its long tongue."

# cat class is a subclass of the Mammal class
class cat(mammal):
    def __init__(self, name):
        super().__init__('cat', name)
    
    def make_sound(self):
        print("meow!")

    def action(self):
        print("purrs and licks paw")

    def __str__(self):
        return f"{self._name} is a clever cat that loves to climb and chase yarn."

# hedgehog class is a subclass of the Mammal class
class hedgehog(mammal):
    def __init__(self, name):
        super().__init__('hedgehog', name)
    
    def make_sound(self):
        print("*silence*")

    def action(self):
        print("rolling around")

    def __str__(self):
        return f"{self._name} is a cute hedgehog, known for making its owner happy."

# siamese class is a subclass of the Cat class
class siamese(cat):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("MEOW!")

    def action(self):
        print("wearing bows and looking pretty")

    def __str__(self):
        return f"{self._name} is a siamese cat, known for its elegance and beauty."

# create instances of each species
def main():
    # creating instances of each species
    frog_instance = frog("naveen")
    hedgehog_instance = hedgehog("odie")
    cat_instance = cat("suzie")
    siamese_instance = siamese("lady")

    # display information about each species
    for animal in [frog_instance, hedgehog_instance, cat_instance, siamese_instance]:
        print(animal)
        animal.show_species()
        animal.make_sound()
        animal.action()
        print()

# testing the program
if __name__ == "__main__":
    main()
