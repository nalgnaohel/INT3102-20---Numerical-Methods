import numpy as np
import math

def func(x: float):
    return np.round(x * np.exp(x), decimals=6)

def three_points_endpoint(x: list, h: float):
    res = []
    for i in range(len(x)):
        tmp = -3 * func(x[i]) + 4 * func(x[i] + h) - func(x[i] + 2 * h)
        tmp *= 1 / (2 * h)
        res.append(tmp)
    return res

def three_points_midpoint(x: list, h: float):
    res = []
    for i in range(len(x)):
        tmp = func(x[i] + h) - func(x[i] - h)
        tmp *= 1 / (2 * h)
        res.append(tmp)
    return res

def five_points_endpoint(x: list, h: float):
    res = []
    for i in range(len(x)):
        tmp = -25 * func(x[i]) + 48 * func(x[i] + h) - 36 * func(x[i] + 2 * h)
        tmp += 16 * func(x[i] + 3 * h) - 3 * func(x[i] + 4 * h)
        tmp /= (12 * h)
        res.append(tmp)
    return res

def five_points_midpoint(x: list, h: float):
    res = []
    for i in range(len(x)):
        tmp = func(x[i] - 2 * h) - 8 * func(x[i] - h)
        tmp += 8 * func(x[i] + h) - func(x[i] + 2 * h)
        tmp /= (12 * h)
        res.append(tmp)
    return res

def second_derivative_midpoint(x: list, h: float):
    res = []
    for i in range(len(x)):
        tmp = func(x[i] + h) - 2 * func(x[i]) + func(x[i] - h)
        tmp /= (h ** 2)
        res.append(tmp)
    return res

x = [(1.8 + 0.1 * i) for i in range(6)]
fx = [func(i) for i in x]
print("f(x): ", fx)
print("Three-point endpoint formula: ", three_points_endpoint(x, x[1] - x[0]))
print("Three-point midpoint formula: ", three_points_midpoint(x, x[1] - x[0]))
print("Five-point endpoint formula: ", five_points_endpoint(x, x[1] - x[0]))
print("Five-point midpoint formula: ", five_points_midpoint(x, x[1] - x[0]))
print("Second derivative midpoint formula: ", second_derivative_midpoint(x, x[1] - x[0]))