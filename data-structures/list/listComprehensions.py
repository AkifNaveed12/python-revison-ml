# instead of
squares = []
for x in range(1,6):
    squares.append(x **2)
print(squares)

# we can write
Squares = [x ** 2 for x in range(1,6)]
# general structure : [expression for item in iterable]

# with condition
even_no = [x for x in range(10) if x % 2 == 0]
print(Squares)
print(even_no)