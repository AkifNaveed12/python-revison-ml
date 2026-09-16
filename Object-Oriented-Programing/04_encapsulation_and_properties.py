

class MLPipeline:
    def __init__(self, name):
        self.name = name
        self._is_trained = False  # Single underscore = convention for protected/internal
        self.__secret_key = "12345"  # Double underscore = name mangling (private)

    # Read-only getter property
    @property
    def status(self):
        return "Trained" if self._is_trained else "Untrained"

    def train(self):
        print("Training pipeline...")
        self._is_trained = True

# Usage
pipeline = MLPipeline("ImageClassifier")
print("Pipeline status:", pipeline.status)  # Access like an attribute, not a method

pipeline.train()
print("Pipeline status:", pipeline.status)