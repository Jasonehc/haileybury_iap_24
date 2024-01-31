import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

# Creation of the main perceptron object.
class Perceptron(object):
    #Initiating the learning rate and number of iterations.
    def __init__(self, learning_rate=0.1, iterations=20):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.zeros(3)
        self.end_weights = [[], [], []]
    # Defining fit method for model training.
    def train(self, x, y):
        self.weights = np.zeros(1 + x.shape[1])
        for i in range(self.iterations):
            wrong_point = False
            print("Starting iteration", i)
            for xi, target in zip(x, y):
                if target != self.predict(xi):
                    wrong_point = True
                    update = self.learning_rate * (target - self.predict(xi))
                    self.weights[1:] += update*xi
                    self.weights[0] += update

                    self.end_weights[0].append(self.weights[0])
                    self.end_weights[1].append(self.weights[1])
                    self.end_weights[2].append(self.weights[2])
            if not wrong_point:
                break
    
    # Net Input method for summing the given matrix inputs and their corresponding weights.
    def net_input(self, x):
        return np.dot(x, self.weights[1:]) + self.weights[0]

    # Predict method for predicting the classification of data inputs.
    def predict(self, x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)

# Data retrieval and preperation.
y = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
x = y.iloc[0:100, [0, 2]].values

y = y.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# Model training and evaluation.
Classifier = Perceptron(learning_rate=0.01, iterations=50)
Classifier.train(x, y)

def visualize(points, line_weights):
    n = len(line_weights[0])
    
    plt.xlim(4, 7)
    plt.ylim(0, 10)

    for i in range(n):
        plt.clf()
        plt.xlim(4, 7)
        plt.ylim(0, 7)
        plt.scatter(points[:50, 0], points[:50, 1], color='red')
        plt.scatter(points[50:100, 0], points[50:100, 1], color='blue')
        
        slope = -line_weights[2][i]/line_weights[1][i]
        intercept = line_weights[0][i]
        x_vals = np.linspace(4,7, 100)
        y_vals = [slope*i+intercept for i in x_vals]
        plt.plot(x_vals, y_vals)
        plt.pause(.5)

# Plotting
end_weights = Classifier.end_weights
print(end_weights)
visualize(x, end_weights)
