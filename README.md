This is Python OOP example lesson

**step 1**
- create an Animal class as our Parent
```python
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


```
**step 2**
- create reptile class as the child class 
- Why? so we can Inherit from our parent 
- Abstract 

**step 3**
- create snake class as child of reptile

**step 4**
- create a Python class.

```__name__``` and ```__main__``` are used to check if the code is run from current file/directly for different file/importing it
- we will create 2 files and use ```__name__``` and ```__main__``` in both files and the outcome will show the difference

# getter and setter code along
```python
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company
```
- getters method with hidden information
```
    def getStudent(self, value):
        self.__name # __ are used to hide the data
```
- defining a setters funtions
```python

    def setStudent(self, value):
        self.__name = value
```
student_object = Student("Shahrukh", "Sparta Global")

print("Student name is " + student_object.setStudent())
```

**Second Iteration**
```
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company
- Using @property decorator with Student function
```        
    @property 
    def Student(self, value):
        print(" This setter method in student data")
        self.__name # __ are used to hide the data
```
- A decorator in Python is any callable python object that is used to modify a function or a class
```
    @Student.setter
    def Student(self, value):
        print(" calling @student.student method")
        self.__name = value
```
- creating an object with required information
```
student_object = Student("Shahrukh ", "Sparta Global")

print("Student name is " + student_object.name)
print("=" * 34)
print("student works in "+ student_object.company)
```