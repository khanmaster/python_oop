# getter and setters
# why - use cases
# To hide the data - Seperation of concern

# syntax 2 functions 1 to get information and to set information

# create a class called student
# Step 1
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def getStudent(self, value):
        self.__name # __ are used to hide the data

    def setStudent(self, value):
        self.__name = value

student_object = Student("Shahrukh", "Sparta Global")

print("Student name is " + student_object.setStudent())

# step 2 second iteration

class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    @property # A decorator in python is any callable python object that is used to modify a fucntion or a class
    def Student(self, value):
        print(" This setter method in student data")
        self.__name # __ are used to hide the data

    @Student.setter
    def Student(self, value):
        print(" calling @student.student method")
        self.__name = value

student_object = Student("Shahrukh ", "Sparta Global")

print("Student name is " + student_object.name)
print("=" * 34)
print("student works in "+ student_object.company)
