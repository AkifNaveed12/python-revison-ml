
# indexing & slicing
text = "Machine Learning"

print(text[0])   # M
print(text[-1])  # g
print(text[0:7]) # Machine

# imutability
# text[0] = "m" not possible we have to craete a new string
# print(text[0])

# string methods

# .lower()

text = "HELLO"
print(text.lower())
text.lower()

# .upper()
print(text.upper())

#  .strip() -> removes unnecessary spaces initial and at end
demo = "             hello             "
print(demo.strip().lower())

# .replace()   -> used to replacing in-consistent data
text = "i am a SW Eng!"
text = text.replace("SW", "Software")
print(text)

# .split() -> separates the words of the sentences on the bases of the space
sentence = "machine learning is powerfull!"
words = sentence.split()
print(words)

data = "Ali,Ahmed,Sara"

names = data.split(",")
print(names)

# .join()
words = ["machine", "learning"]
sentence = " ".join(words)
print(sentence)

print(",".join(["Python", "SQL", "ML"]))

# split() → string → list
# join() → list → string

# membership
text = "hello akif"
print("akif" in text)


# startswith()/endswith()
filename = "dataset.csv"

print(filename.endswith(".csv"))
print(filename.startswith("Data"))

# f-strings
name = "Akif"
score = 95

message = f"{name} scored {score}"

print(message)

accuracy = 0.93456

print(f"Accuracy: {accuracy:.2%}")

# len()
print(len(filename))

raw_data = "   Machine Learning, Artificial Intelligence, Data Science   "
clean_data = raw_data.strip().lower().split(",")
for i in clean_data:
    print(i)