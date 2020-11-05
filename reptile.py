# creating a reptile class as a child class of our Animal class
from animal import Animal
# Syntax to import files and classes

class Reptile(Animal):
    def __init__(self):

        super().__init__() # Super key word is used to inherit everything from a parent class
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chamber = [3, 4]

    # creating function for out Reptile class
    def seek_heat(self):
        return "it's freezing looking for a sun shine!"

    def hunt(self):
        return "working really hard to catch a meal....."

    def use_venum(self):
        return "if I've got it I'm using it"

# Let's create an object of our Reptile class to utilise the amazing functionalities of OOP
reptile_object = Reptile()

print(reptile_object.eat())
print(reptile_object.breathe())
print(reptile_object.procreate())
print("the above functionality is inherited from our Animal/Parent class")

print(reptile_object.use_venum())

print(reptile_object.seek_heat())
print(reptile_object.hunt())

