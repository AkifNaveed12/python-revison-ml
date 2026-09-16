# Iterator An iterable
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# generators
def numbers():
    for i in range(5):
        yield i
for number in numbers():
    print(number)
    
# list → stores everything
# generator → produces values as needed