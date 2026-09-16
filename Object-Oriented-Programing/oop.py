# creating classes + objects

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        
    def display(self):
        print(self.name, self.cgpa)

student = Student("Akif", 3.7)
student.display()

# class → blueprint
# object → instance
# __init__ → constructor
# self → current object
# attributes → name, cgpa
# methods → display()