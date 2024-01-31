import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap

# Creation of the main perceptron object.
class Perceptron(object):
    #Initiating the learning rate and number of iterations.
    def __init__(self, learning_rate=0.5, iterations=10):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.zeros(3)
    
    # Defining fit method for model training.
    def train(self, x, y):
        self.weights = np.zeros(1 + x.shape[1])
        for i in range(self.iterations):
            print("Starting iteration", i)
            for xi, target in zip(x, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update*xi
                self.weights[0] += update
            print(self.weights)
            #self.plot_decision_line(x, y)
        return self
    
    # Predict method for predicting the classification of data inputs.
    def predict(self, x):
        return np.where(np.dot(x, self.weights[1:]) + self.weights[0](x) >= 0.0, 1, -1)
    
    def plot_decision_line(self, x, y):
        # setup marker generator and color map
        slope = -self.weights[2]/self.weights[1]
        intercept = self.weights[0]

# Data retrieval and preperation.
y = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
print(y)
x = y.iloc[0:100, [0, 2]].values
print(x)
plt.scatter(x[:50, 0], x[:50, 1], color='red')
plt.scatter(x[50:100, 0], x[50:100, 1], color='blue')
plt.show()
y = y.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# Model training and evaluation.
Classifier = Perceptron(learning_rate=0.01, iterations=50)
Classifier.train(x, y)
