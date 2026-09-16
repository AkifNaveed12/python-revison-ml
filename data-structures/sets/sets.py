# An unordered collection of the unique elements
numbers = {1, 2, 3, 4}

# duplicates disappear
numbers = {1,2,2,2,2,4,3,3,3,3}
print(numbers)

# The biggest AI/data-related use is uniqueness and membership checking.
categories = {"cat", "dog", "horse"}
#Very fast membership checking is one reason sets are useful.
print("cat" in categories)

# adding/removing
categories.add("bird")
categories.remove("dog")#raises an error if the item is not present

categories.discard("dog")# doesn't raises an error if the item isn't present

# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# operation 01: intersection
print(a & b) # common elements {3,4}

# operation 02: Union
print(a | b)
# {1, 2, 3, 4, 5, 6}

# operation 03: Difference
print(a - b)
# {1, 2}
# operation 04: symmetric difference
print(a ^ b)
# {1,2,5,6}

