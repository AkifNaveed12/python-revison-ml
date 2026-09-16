# writing into a file
with open("filetest.txt", "w") as file: # "w" -> overrites, "a" appends
    file.write("Machine Learning! ")

with open("filetest.txt", "a") as file: # auto creates file if isnt present
    file.write("hello im akif!")
    
    
# writing files
with open("filetest.txt", "r") as file: # with automatically handles the file closing
    content = file.read()

print(content)

# reading lines opt 1
with open("filetest.txt", "r") as file:
    lines = file.readlines()
    
# reading lines opt 2
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

