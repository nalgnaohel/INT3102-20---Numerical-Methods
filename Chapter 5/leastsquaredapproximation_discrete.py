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

#Ex 3
x = [1, 1.1, 1.3, 1.5, 1.9, 2.1]
y = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]
for i in range(1, 4):
    a, y_fit = least_squares_approximation(x, y, i)
    print("Coefficients:", end= ' ')
    print(a, "\n-----------")
    print(y_fit - y)
    x_fit = x.copy()

    plt.scatter(x, y, label='Data')
    plt.plot(x_fit, y_fit, color='red', label='Fitted Curve degree' + str(i))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()