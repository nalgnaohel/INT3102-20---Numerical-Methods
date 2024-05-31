import numpy as np
import matplotlib.pyplot as plt

def least_squares_approximation(x: list, y: list, degree):
    m = len(x)
    X = np.zeros((degree + 1, degree + 1))
    for i in range(degree + 1):
        for j in range(degree + 1):
            for id in range(m):
                X[i][j] += x[id] ** (i + j)
    
    Y = np.zeros(degree + 1)
    for i in range(degree + 1):
        for id in range(m):
            Y[i] += y[id] * (x[id] ** i)
    
    a = np.linalg.solve(X, Y)
    y_fit = np.zeros(m)
    for i in range(m):
        for deg in range(degree + 1):
            y_fit[i] += a[deg] * (x[i] ** deg)
    return a, y_fit

x = [0.25 * i for i in range(5)]
y = [1.0000, 1.2840, 1.6487, 2.1170, 2.7183]
a, y_fit = least_squares_approximation(x, y, 2)
print("Coefficients:", end= ' ')
print(a, "\n-----------")
print(y_fit - y)
x_fit = x.copy()

plt.scatter(x, y, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()