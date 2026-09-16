# Dunder methods
Dunder methods (short for Double Underscore methods) are special pre-defined methods in Python that start and end with two underscores, like __init__, __str__, or __len__. They are often called magic methods.

## Why Are They Used?
In Java, if you want to print an object or find its length, you usually write custom helper methods like obj.toString() or obj.getSize().

In Python, dunder methods allow your custom classes to integrate directly with Python's built-in functions, operators, and syntax. By implementing dunder methods, your custom objects behave just like native Python data types (like lists, dictionaries, or numbers).

## Key AI/ML Use Cases
__init__: Constructor. Sets up initial hyperparameters, layers, or configurations.

__str__ / __repr__: Controls how your object prints to the console when debugging.

__len__: Lets you call len(your_object). Essential in PyTorch Datasets to count total samples.

__getitem__: Enables indexing via your_object[index]. Used in ML pipelines to fetch training samples.

__call__: Allows an instance of a class to be called like a function: model(input_data). Used in PyTorch, TensorFlow, and Scikit-Learn for forward passes and transformations.