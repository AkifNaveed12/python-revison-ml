# instead of
names = ["Ali", "Ahmad", "Sara"]
for i in range(len(names)):
    print(i, names[i])
    
# we will be using enumerate
for i, name in enumerate(names, start=1):
    print(i, name)
# enumerate() gives you index + value.

features = ["age", "salary", "experience"]
for i, feature in enumerate(features):
    print(i, feature)