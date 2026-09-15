# types of function parameters

# default parameters ( by-default value incase if user doesnt gives we have the default one)

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Akif Naveed"))

print(greet("Akif Naveed Malik", "Welcome, how are you? "))


# keyword arguments (order/ position of the arguments doesnt matters we cn pass the arguments in any order just mention the parameter = argument)
def introduce(name, age, profession):
    return f"{name} is {age} and works as a {profession}."
print("Akif", 21, "Student")
print(
    introduce(
    profession="Developer",
    name="Akif Naveed",
    age=20
))

def calculate(a, b):
    addition = a + b
    multiplication= a * b
    return addition, multiplication

sum_result, product_result = calculate(2,4)

print(sum_result)
print(product_result)

#*args Variable positional arguments: Sometimes you don't know beforehand how many positional arguments a function will receive.

def add(*args):   #args is a tupple here * is more imp even *numbers also works and does the same thing
    return sum(args)  # *args are like a tupple

print(add(1,2,3,4))
print(add(5,10))

# **kwargs Variable keyword arguments: **kwargs handles an arbitrary number of keyword arguments.
def show_info(**kwargs):
    print(kwargs) # **kwargs dictionary

show_info(
    name="Akif",
    age=21,
    field="AI"
    )

def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


create_profile(
    name="Akif",
    field="AI",
    university="University"
)


# combining normal parameters *args, **kwargs
def example(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
example(
    "Akif",
    10,
    20,
    30,
    age=21,
    field="AI"
)

# unpacking with * and ** : its the opposite direction we unpack the stuff
# suppose : numbers = [10, 20, 30] and 
#def add(a, b, c):
    # return a + b + c
# we can do
# add(*numbers), python turn that into add(10, 20, 30)

numbers = [10, 20, 30]
def add(a, b, c):
    return a + b + c
print(add(*numbers))

# same with ** for dictionaries
def introduce(name, age):
    print(f"{name} is {age} years old.")
    
person = {
    "name": "Akif",
    "age": 21
}

introduce(**person)

# positional-only arguments: force arguments to be positional
def calculate(a, b, /):
    return a + b

calculate(10, 20) # thisworks but this calculate(a=10, b=20) doesnt



# You can also force arguments to be keyword-only
def train_model(data, *, epochs, learning_rate):
    print(data, epochs, learning_rate)
train_model(
    "training_data",
    epochs=10,
    learning_rate=0.01
) # this works

# his doesnt works
# train_model("training_data", 10, 0.01)

