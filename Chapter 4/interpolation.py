import numpy as np
import matplotlib as plt

def f(x: float):
    return np.exp(2 * x) * np.cos(3 * x)

def lagrange(x: list, y:list, x_estimate: float):
    y_estimated = 0
    for i in range(len(x)):
        lx, lxi = 1, 1
        for j in range(len(x)):
            if i != j:
                lx *= (x_estimate - x[j])
                lxi *= (x[i] - x[j])
        y_estimated += lx / lxi * y[i]
    
    return y_estimated

def newton(x: list, y: list, x_estimate: float):
    n = len(x)
    diff = np.zeros((n, n))
    for i in range(n):
        diff[i][0] = y[i]
    
    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
    
    print("Diff matrix:")
    for i in range(n):
        for j in range(n):
            print(diff[i][j], end=' ')
        print("")
    print("+++++++++++")    
    
    h = x[1] - x[0]
    r = (x_estimate - x[0]) / h
    coeff = 1

    y_estimated = diff[0][0]
    for i in range(1, n):
        coeff *= r - (i - 1)
        coeff /= i
        y_estimated += diff[0][i] * coeff
    
    return y_estimated


x = [0, 0.3, 0.6]
y = [f(i) for i in x]
x_estimate = 0.5
print("x: ", x)
print("y: ", y)
print("------------\nLagrange:", end=' ')
print(lagrange(x, y, x_estimate), end = ' ')
print(f(x_estimate)) #Ex 13 - Lagrange
print("------------\nNewton:", end=' ')
x = [-0.25 * i for i in range(4)]
y = [1.101, 0.33493750, -0.002475000, -0.07181250]
x_estimate = - 1 / 3
print(newton(x, y, x_estimate), end = ' ')
print(f(x_estimate)) #Ex 3a - Newton
print("+++++++++++-------")
x = [0.1 * i for i in range(1, 5)]
y = [-0.62049958, 0.28398668, 0.00660095, 0.24842440]
x_estimate = 0.25
print(newton(x, y, x_estimate), end = ' ')
print(f(x_estimate)) #Ex 3b - Newton