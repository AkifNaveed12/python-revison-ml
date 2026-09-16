class LinearRegressionModel:
    # Class attribute (shared by all instances)
    framework = "PyTorch"

    def __init__(self, learning_rate: float, epochs: int):
        # Instance attributes (unique to each instance)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None  # Will be initialized during training
        self.bias = None

    def fit(self, X, y):
        print(f"Training using {self.framework} with LR={self.learning_rate} for {self.epochs} epochs.")

# Usage
model = LinearRegressionModel(learning_rate=0.01, epochs=100)
model.fit(X=[1, 2, 3], y=[2, 4, 6])