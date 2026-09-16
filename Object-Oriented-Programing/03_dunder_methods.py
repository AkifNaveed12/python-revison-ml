# 03_dunder_methods.py

class CustomDataset:
    """Simulates a PyTorch style Dataset"""
    def __init__(self, data):
        self.data = data

    # 1. Called when checking len(obj)
    def __len__(self):
        return len(self.data)

    # 2. Called when indexing obj[index]
    def __getitem__(self, idx):
        return self.data[idx]

    # 3. Called when object is printed: print(obj)
    def __str__(self):
        return f"CustomDataset(size={len(self.data)})"

    # 4. Makes the instance callable like a function: obj(x)
    def __call__(self, batch_size):
        return f"Processing batch of size {batch_size}"

# Usage
dataset = CustomDataset(data=[10, 20, 30, 40, 50])

print(dataset)              # Trigger __str__
print("Dataset size:", len(dataset))  # Trigger __len__
print("Element at index 2:", dataset[2])  # Trigger __getitem__
print(dataset(batch_size=32))  # Trigger __call__