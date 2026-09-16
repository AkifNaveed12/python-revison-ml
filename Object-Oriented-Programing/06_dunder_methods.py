# 06_dunder_methods.py

class MLDataset:
    def __init__(self, samples):
        # 1. Constructor: Initializes instance attributes
        self.samples = samples

    def __len__(self):
        # 2. Triggered when you run: len(obj)
        return len(self.samples)

    def __getitem__(self, index):
        # 3. Triggered when you access by index: obj[index]
        return self.samples[index]

    def __str__(self):
        # 4. Triggered when you run: print(obj) or str(obj)
        return f"MLDataset with {len(self.samples)} items"

    def __call__(self, batch_size):
        # 5. Triggered when you call the instance like a function: obj(32)
        return f"Fetching batch of size {batch_size} from dataset."


# --- Execution / Usage ---

dataset = MLDataset(samples=["feature1", "feature2", "feature3", "feature4"])

# Triggers __str__
print(dataset)  # Output: MLDataset with 4 items

# Triggers __len__
print("Total dataset size:", len(dataset))  # Output: Total dataset size: 4

# Triggers __getitem__
print("Sample at index 2:", dataset[2])  # Output: Sample at index 2: feature3

# Triggers __call__ (Treating instance like a function)
print(dataset(batch_size=2))  # Output: Fetching batch of size 2 from dataset.