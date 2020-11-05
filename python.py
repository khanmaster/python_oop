# Creating a python class as child class of our Snake class

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    # creating functions for our python class

    def digest_large_prey(self):
        return " Yum Yummyyy...."

    def clim(self):
        return "up we go....."

    def shed_skin(self):
        return "time to grow up.... fast......myself!"

python_object = Python()

# creating an object of our python class

print(python_object.breathe()) # function from our Animal class
print(python_object.hunt()) # function from our Reptile class
print(python_object.use_venum())# fucntion from our Snake class
print(python_object.shed_skin()) # function from our python class
