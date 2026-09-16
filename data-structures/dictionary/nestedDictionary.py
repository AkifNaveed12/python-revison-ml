model = {
    "name": "Linear Regression",
    "parameters": {
        "learning_rate": 0.01,
        "epochs": 100
    }
}
# accessing nested dictionary
print(model["parameters"]["learning_rate"])

# conversion into dictionary from2 lists

keys = ["name", "age", "field"]
values = ["Akif", 21, "AI"]
student = dict(zip(keys, values))
print(student)