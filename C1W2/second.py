import scipy.linalg as la
import numpy as np


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


# a = np.array([[1, 1], [1, 15]])
# b = np.array([f(1), f(15)])
# a = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 225]])
# b = np.array([f(1), f(8), f(15)])
a = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = np.array([f(1), f(4), f(10), f(15)])

answer = la.solve(a, b)
print(answer)
