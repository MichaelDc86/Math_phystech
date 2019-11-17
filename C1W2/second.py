import scipy.linalg as la
import numpy as np


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


rez_1 = f(1)
rez_2 = f(2)
# print(rez_1)
# print(rez_2)
a = np.array([[1, 1], [1, 15]], dtype=np.float32)
# print(np.linalg.inv(a))
b = np.array([rez_1, rez_2]).reshape(2, 1)
# print(b)
# print(b.shape)
# print(a)
answer = la.solve(a, b)
print(answer)
