# Creating an Animal class as PARENT/BASE/SUPER class

class Animal:

    def __init__(self): # initialising the Animal class
        self.alive = True # creating an attribute/variable
        self.spine = True
        self.lungs = True
        self.eyes = True

    # create behaviours as fucntions/methods
    def breathe(self):
        return "Keep breathing to stay alive "

    def move(self):
        return "left to right and up and down...."

    def eat(self):
        return "Nom Nom Nom"

    def procreate(self):
        return "find partner"

# instantiate our class/ create and object

cat = Animal() # creating an object of Animal class
# cat as child has inherited everything from Animal / parent class
# Absracted eat() method from our parent class
# print(cat.eat())

