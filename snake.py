# Creating a snake class as child class of Reptile

from reptile import Reptile
class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    # creating functions for our Snake class
    def use_tongue_to_smell(self):
        return "I use tongue to taste "

snake_object = Snake()

# print(snake_object.limbs)
# print(snake_object.breathe())
# We have double inheritance and Encapsulated in fucntions in parent classes
