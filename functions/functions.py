# reuseable block of code

# syntax 
# def function_name(paameters):
#     #function body
#     return value

def add_no(a, b):
    return a+b

print(add_no(10,5)) #parametrs 10, 5 are passed to the function add_no

def square(number):
    return number * number
print(square(10)) # parameter 10 is passed to the function


# parameter vs arguments
# assume a function def greet(name): -> here name is the paramter (dummy value to understand what this function wants)
# and when we call greet("Akif") -> here "Akif" is teh argument that is passed to the function greet

# so parameter = placeholder , argument + actual value


# return vs print

def display(name):
    return name
result = display("Ali")
print(result)
print(display("ahad"))

def display2(name):
    return name
result2 = display2("Arslan")
print(result2)
result3 = display2("ahmad")
print(result3)

