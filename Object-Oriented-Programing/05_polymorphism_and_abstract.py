# 05_polymorphism_and_abstract.py

from abc import ABC, abstractmethod

# Abstract Base Class enforcing an interface
class BaseModel(ABC):
    
    @abstractmethod
    def predict(self, input_data):
        """Every subclass must implement this method"""
        pass

class DecisionTree(BaseModel):
    def predict(self, input_data):
        return f"DecisionTree prediction for {input_data}"

class SupportVectorMachine(BaseModel):
    def predict(self, input_data):
        return f"SVM prediction for {input_data}"

# Polymorphic execution function
def evaluate_model(model: BaseModel, data):
    print(model.predict(data))

# Usage
dt = DecisionTree()
svm = SupportVectorMachine()

evaluate_model(dt, [1, 2, 3])
evaluate_model(svm, [1, 2, 3])