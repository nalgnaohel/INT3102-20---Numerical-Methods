import numpy as np
import matplotlib as plt

def f(x: float):
    return np.exp(x)

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


x = [0, 1, 2, 3]
y = [f(i) for i in x]
x_estimate = 2.5
print("x: ", x)
print("y: ", y)
print("------------\nLagrange:", end=' ')
print(lagrange(x, y, x_estimate), end = ' ')
print(f(x_estimate))
print("------------\nNewton:", end=' ')
print(newton(x, y, x_estimate), end = ' ')
print(f(x_estimate))
# print("------------\nCubic Spline:", end=' ')
# print(newton(x, y, x_estimate), end = ' ')
# print(f(x_estimate))