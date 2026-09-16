numbers = [10, 20, 30]

print(sum(numbers))
print(min(numbers))
print(max(numbers))

# importance of key
students = [
    ("Ali", 85),
    ("Ahmed", 92),
    ("Sara", 78)
]

top_student = max(students, key=lambda x: x[1])