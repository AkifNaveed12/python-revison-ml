# these are the immutable sequences(can't modify)
point = (10, 20)
# point[0] = 50 # TypeError

# Use a list when the collection needs to change.
# Use a tuple when the values represent a fixed group of related values.


# index and slicing
point = (10, 20, 30)
print(point[0])  # 10
print(point[-1]) # 30
print(point[1:]) # (20,30)

# packing & unpacking
point = 10,20,30 # packing
x, y, z = point # unpacking

first, *middle, last = (1,2,3,4,5,6,7,8,9)

# returning tuple values
def get_dimensions():
    return 1920, 1080
width, height = get_dimensions()