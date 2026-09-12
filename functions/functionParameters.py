# types of function parameters

# default parameters ( by-default value incase if user doesnt gives we have the default one)

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Akif Naveed"))

print(greet("Akif Naveed Malik", "Welcome, how are you? "))


# keyword arguments (order/ position of the arguments doesnt matters we cn pass the arguments in any order just mention the parameter = argument)