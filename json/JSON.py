import json

# python dictionary -> JSON
data = {
    "model" : "linear regression",
    "accuracy": 0.92,
    "features": ["age", "salary"]
}

json_data = json.dumps(data) # dumps converts python objects into JSON string
print(json_data)

# JSON -> python dictionary
# loads() → JSON string → Python object.
data = json.loads(json_data)
print(data["model"])

# json file writing

with open("model.json", "w") as file:
    json.dump(data, file, indent=4)

# file reading
with open("model.json", "r") as file:
    data = json.load(file)
# dump  → Python → JSON file
# dumps → Python → JSON string

# load  → JSON file → Python
# loads → JSON string → Python
