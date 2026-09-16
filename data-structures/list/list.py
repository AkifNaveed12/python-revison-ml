# list is ordered, mutale, can contain duplicates, can contain diff data type values
numbers = [1,2,3,4]
data = [10, "Python", 3.14, True]

print(numbers)
print(data)

# python uses zero based indexing 

print(numbers[0])
print(numbers[2])
print(numbers[1])
# negitive indexing starts form the end  -1 onwards
print(numbers[-1]) # 4
print(numbers[-2])

# slicing : Slicing extracts a portion of a list.
# list[start:stop:step]
# start is included, stop is excluded.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

print(numbers[:3]) #[10, 20,30]
print(numbers[2:]) #[30, 40,50]
print(numbers[::2]) # [10, 30, 50]
print(numbers[::-1]) # [50, 40, 30, 20, 10]


# mutability
numbers = [10, 20, 30]
numbers[1] = 150
print(numbers)

# adding/ removing elements

Numbers = [1, 2, 3]
Numbers.append(4)
print(Numbers)

# extends : adds multiple elements
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)

# insertions
numbers = [10, 20, 30, 40]
# list.insert(index, value)
numbers.insert(2, 55)
print(numbers)

# remove : removes the 1st matching value
numbers.remove(55)
print(numbers)

# pop : removes item by index and returns it
numbers = [10, 20, 30]
removed = numbers.pop(1) # if we dont provide index to pop by default it removes the last element
print(removed)
print(numbers)

# sorting : .sort() modifies the original list
numbers = [5,3,2,1]
numbers.sort()# by default ascending order
print(numbers) 
#for descending
numbers.sort(reverse=True)
print(numbers)

# .sorted(): creates a sorted list, original list remains unchanged
numbers = [5, 4,  3, 2, 1]
sorted_no = sorted(numbers)
print(numbers)
print(sorted_no)

# key with sorting
students = [
    ("akif", 85),
    ("Hamza", 92),
    ("Sara", 78)
]
# we have to sort according to the marks
students.sort(key=lambda student: student[1], reverse=True)
print(students)

# membership : check weather something exists or not

numbers = [100, 200, 500, 700, 1000]
print(5 in numbers)
print(1000 in numbers)

print(20 not in numbers)
print(1000 not in numbers)

# nested listing
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(data[0])
print(data[0][0]) # data[row][column]

# lists unpacking
features = [10, 20, 30]

a, b, c = features
print(a)
print(b)
print(c)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)
print(*middle)
print(last)

# copy vs nested-list coping
data = [[1, 2], [3, 4]]

new_data = data.copy()
print(new_data)