import numpy as np
from math import sin, exp
import scipy
from scipy import optimize as opt

# x_range = np.arange(1, 30, 0.1)
# x_range = np.array([2])
# x_range = np.array([30])
x_range = np.array([10])


# def f(t):
#     for x in t:
#         return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
# def f(x):
#     return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def h(x):
    return int(f(x))


# minimum = opt.minimize(f, x0=x_range, method='BFGS')
minimum = opt.minimize(h, x0=x_range, method='BFGS')
# minimum = opt.differential_evolution(f, [(1, 30)])
# minimum = opt.differential_evolution(h, [(1, 30)])
# minimum = f(np.array([4.13630013]))
# minimum = h(np.array([30.]))
print(minimum)
