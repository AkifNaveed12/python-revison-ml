squares = {x: x ** 2 for x in range(5)}
# key : value's expression for range
print(squares)

# conditional filtering
scores = {"loss": 0.02, "accuracy": 0.95, "val_loss": 0.12, "val_accuracy": 0.88}
# Keep only accuracy metrics (> 0.80)
high_acc = {k: v for k, v in scores.items() if "accuracy" in k and v > 0.80}
print(high_acc)
# Output: {'accuracy': 0.95, 'val_accuracy': 0.88}

# Key-Value Inversion / Remapping
labels = ["cat", "dog", "bird"]

# Map each class string to a unique integer ID
label_to_id = {label: idx for idx, label in enumerate(labels)}
print(label_to_id)
# Output: {'cat': 0, 'dog': 1, 'bird': 2}

# Invert it back to map predicted integer IDs to class strings
id_to_label = {idx: label for label, idx in label_to_id.items()}
print(id_to_label)
# Output: {0: 'cat', 1: 'dog', 2: 'bird'}