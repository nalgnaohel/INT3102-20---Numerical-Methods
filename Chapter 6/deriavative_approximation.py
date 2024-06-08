import numpy as np
import math

def func(x: float):
    return np.round(np.exp(x) - 2 * (x ** 2) + 3 * x - 1, decimals=4)

def three_points_endpoint_forward(x: list, h: float):
    res = []
    for i in range(len(x) - 2):
        tmp = -3 * func(x[i]) + 4 * func(x[i] + h) - func(x[i] + 2 * h)
        tmp *= 1 / (2 * h)
        res.append(tmp)
    return res

def three_points_midpoint(x: list, h: float):
    res = []
    for i in range(1, len(x) - 1):
        tmp = func(x[i] + h) - func(x[i] - h)
        tmp *= 1 / (2 * h)
        res.append(tmp)
    return res

def three_points_endpoint_backward(x: list, h: float):
    res = []
    for i in range(2, len(x)):
        tmp = 3 * func(x[i]) - 4 * func(x[i] - h) + func(x[i] - 2 * h)
        tmp *= 1 / (2 * h)
        res.append(tmp)
    return res

def five_points_endpoint_forward(x: list, h: float):
    res = []
    for i in range(len(x) - 4):
        tmp = -25 * func(x[i]) + 48 * func(x[i] + h) - 36 * func(x[i] + 2 * h)
        tmp += 16 * func(x[i] + 3 * h) - 3 * func(x[i] + 4 * h)
        tmp /= (12 * h)
        res.append(tmp)
    return res

def five_points_midpoint(x: list, h: float):
    res = []
    for i in range(2, len(x) - 2):
        tmp = func(x[i] - 2 * h) - 8 * func(x[i] - h)
        tmp += 8 * func(x[i] + h) - func(x[i] + 2 * h)
        tmp /= (12 * h)
        res.append(tmp)
    return res

def five_points_endpoint_backward(x: list, h: float):
    res = []
    for i in range(4, len(x)):
        tmp = 25 * func(x[i]) - 48 * func(x[i] - h) + 36 * func(x[i] - 2 * h)
        tmp += -16 * func(x[i] - 3 * h) + 3 * func(x[i] - 4 * h)
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

x = [0.5, 0.6, 0.7]
fx = [np.round(np.sin(i), decimals=4) for i in x]
print("f(x): ", fx)
print("Three-point endpoint formula: ", three_points_endpoint_forward(x, x[1] - x[0]), ' ', three_points_endpoint_backward(x, x[1] - x[0]))
print("Three-point midpoint formula: ", three_points_midpoint(x, x[1] - x[0]))
dx_est = np.array([three_points_endpoint_forward(x, x[1] - x[0])[0], three_points_midpoint(x, x[1] - x[0])[0], three_points_endpoint_backward(x, x[1] - x[0])[0]])
dx = np.array([np.cos(i) for i in x])
print(dx_est)
print("Error: ", dx - dx_est)
# print("Five-point endpoint formula: ", five_points_endpoint(x, x[1] - x[0]))
# print("Five-point midpoint formula: ", five_points_midpoint(x, x[1] - x[0]))
# print("Second derivative midpoint formula: ", second_derivative_midpoint(x, x[1] - x[0]))\

x = [0.0, 0.2, 0.4]
fx = [func(i) for i in x]
print("f(x): ", fx)
print("Three-point endpoint formula: ", three_points_endpoint_forward(x, x[1] - x[0]), ' ', three_points_endpoint_backward(x, x[1] - x[0]))
print("Three-point midpoint formula: ", three_points_midpoint(x, x[1] - x[0]))
dx_est = np.array([three_points_endpoint_forward(x, x[1] - x[0])[0], three_points_midpoint(x, x[1] - x[0])[0], three_points_endpoint_backward(x, x[1] - x[0])[0]])
dx = np.array([(np.exp(i) - 4 * i + 3) for i in x])
print(dx_est)
print("Error: ", dx - dx_est)