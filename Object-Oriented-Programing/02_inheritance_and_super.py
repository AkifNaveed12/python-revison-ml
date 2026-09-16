# 02_inheritance_and_super.py

class BaseEstimator:
    """Simulating a base machine learning estimator"""
    def __init__(self, model_name: str):
        self.model_name = model_name

    def summary(self):
        print(f"Model Name: {self.model_name}")

class NeuralNetwork(BaseEstimator):
    def __init__(self, model_name: str, layers: int):
        # Call the constructor of the parent class (BaseEstimator)
        super().__init__(model_name)
        self.layers = layers

    def forward(self, x):
        print(f"Passing data through {self.layers} layers...")

# Usage
nn_model = NeuralNetwork(model_name="CustomClassifier", layers=4)
nn_model.summary()  # Inherited method
nn_model.forward(x=[0.5, 0.2])