# -*- coding: utf-8 -*-
"""2. numpy linearRegression-with-CostFn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V1eAdA5KWorgeq9P6vR8x2IME3lLEQ1q
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas

# from: https://ml-cheatsheet.readthedocs.io/en/latest/linear_regression.html#cost-function
#
# We need a cost fn and its derivative...

dataset = pandas.read_csv("data/Advertising.csv").as_matrix()


def cost_function(X, y, weight, bias):
    n = len(X)
    total_error = 0.0
    for i in range(n):
        total_error += (y[i] - (weight * X[i] + bias)) ** 2
    return total_error / n


def update_weights(X, y, weight, bias, alpha):
    weight_deriv = 0
    bias_deriv = 0
    n = len(X)

    for i in range(n):
        # Calculate partial derivatives
        # -2x(y - (mx + b))
        weight_deriv += -2 * X[i] * (y[i] - (weight * X[i] + bias))

        # -2(y - (mx + b))
        bias_deriv += -2 * (y[i] - (weight * X[i] + bias))

    # We subtract because the derivatives point in direction of steepest ascent
    weight -= (weight_deriv / n) * alpha
    bias -= (bias_deriv / n) * alpha

    return weight, bias


def train(X, y, weight, bias, alpha, iters):
    cost_history = []

    for i in range(iters):
        weight, bias = update_weights(X, y, weight, bias, alpha)

        # Calculate cost for auditing purposes
        cost = cost_function(X, y, weight, bias)
        # cost_history.append(cost)

        # Log Progress
        if i % 10 == 0:
            print("iter: " + str(i) + " weight: " + str(weight) + " bias: " + str(bias) + " cost: " + str(cost))

    return weight, bias  # , cost_history


# work out
y = dataset[:, 4].reshape(200, 1)
X = dataset[:, 1].reshape(200, 1)

m = 0
c = 0

alpha = 0.1
iters = 100

# normalise the data
y = y / np.linalg.norm(y, ord=np.inf, axis=0, keepdims=True)
X = X / np.linalg.norm(X, ord=np.inf, axis=0, keepdims=True)

weight, bias = train(X, y, m, c, alpha, iters)


# a picture is worth a thousand words...
_ = plt.plot(X, y, 'o', [0, 1], [bias, weight + bias], '-')
plt.show()