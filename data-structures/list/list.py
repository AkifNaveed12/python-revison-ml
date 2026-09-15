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
print(numbers[::2])