# they store key -> value mappings
student = {
    "name": "Akif",
    "semester": 5,
    "cgpa": 3.7
}
# accessing values
print(student["name"])
print(student["cgpa"]) #KeyError if missing
print(student.get("name")) # None if missing
# we can also provide a default here
print(student.get("age", 0))

# adding updating
student["age"] = 21
# if key exists it updates
student["cgpa"] = 3.8
print(student)

# removing
student.pop("age") # or del student["age"]
print(student)

# checking keys
print("name" in student)
# print("name" in student) checks keys, not values

# iterating 
for key in student:
    print(key)
for value in student.values():
    print(value)
    
# Printing Keys and Values Together
for key, value in student.items():
    print(f"{key}: {value}")
