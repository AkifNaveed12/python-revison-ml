# zip() combines corresponding elements.
names = ["Ali", "Sara", "Ahmad"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(name, score)

# zip() stops at the shortest iterable:
LIST = list(zip([1, 2, 3], ["a", "b"]))
print(LIST)

features = ["age", "salary", "experience"]
values = [21, 50000, 2]

dic = dict(zip(features, values))
print(dic)