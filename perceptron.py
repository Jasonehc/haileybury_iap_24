import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class Perceptron(object):
    def __init__(self, learning_rate, n_iter):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.weights = np.array([0.0, 0.0, 0.0])
        self.end_weights = []

    def fit(self, X, y):
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                print(xi, target)
                predict = self.predict(xi)
                if predict != target:
                    update = self.learning_rate * (target - self.predict(xi))
                    
                    self.weights[1:] += update * xi
                    
                    self.weights[0] += update
                    errors += int(update != 0.0)
                    self.end_weights.append((self.weights[0], self.weights[1], self.weights[2]))
            self.errors_.append(errors)
        return self

    def predict(self, X):
        """Return class label after unit step"""
        if np.dot(X, self.weights[1:]) + self.weights[0] > 0.0:
            return 1
        else:
            return 0

# Obtain data
iris = load_iris()
X = iris.data
y = iris.target
data = np.hstack((X, y[:, np.newaxis]))

labels = iris.target_names
features = iris.feature_names
df = pd.DataFrame(data, columns=iris.feature_names+['label'])
df.label = df.label.map({k:v for k,v in enumerate(labels)})

# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'setosa', -1, 1)

# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values

#Training
ppn = Perceptron(learning_rate=0.01, n_iter=10)

ppn.fit(X, y)

def visualize(points, line_weights):
    line_weights = line_weights
    
    plt.xlim(4, 7)
    plt.ylim(0, 10)

    for weight0, weight1, weight2 in line_weights:
        plt.clf()
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.scatter(points[:50, 0], points[:50, 1], color='red')
        plt.scatter(points[50:100, 0], points[50:100, 1], color='blue')
        
        slope = -weight1/weight2
        intercept = weight0
        print("line is y = " + str(slope) + "x+" + str(intercept))
        x_vals = np.linspace(0,10, 100)
        y_vals = [slope*i+intercept for i in x_vals]
        plt.plot(x_vals, y_vals)
        plt.pause(.1)
    plt.pause(1)

print(ppn.weights)
print(len(ppn.end_weights))

visualize(X, ppn.end_weights)
