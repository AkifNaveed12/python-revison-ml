# lambda functions is a small anonymous function

# normal function is 
def square(x):
    return x ** 2
# lambda :
square = lambda x: x ** 2
print(square(5))

# lambda parameters: expression
students = [
    ("Ali", 80),
    ("Ahmed", 95),
    ("Sara", 88)
]

print(students.sort(key=lambda student: student[1]))



