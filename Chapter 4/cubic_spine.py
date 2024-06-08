import numpy as np
import matplotlib.pyplot as plt

def cubic_spline_coeff(x, y, diff_x0, diff_xn):
    n = len(x)
    d = y.copy()
    h = np.diff(x)
    #Define H, S, and Y matrix. H is a tridiagonal matrix
    H = np.zeros((n, n))
    H[0][0], H[n - 1][n - 1] = 2, 2
    H[0][1], H[n - 1][n - 2] = 1, 1
    for i in range(1, n - 1):
        H[i][i - 1] = h[i - 1] / (h[i - 1] + h[i])
        H[i][i] = 2
        H[i][i + 1] = h[i] / (h[i - 1] + h[i])
    print("H:")
    print(H, "\n-------")
    Y = np.zeros(n)
    Y[0] = 6 * ((y[1] - y[0]) / h[0] - diff_x0) / h[0]
    Y[n - 1] = 6 * (diff_xn - (y[n - 1] - y[n - 2] / h[n - 2])) / h[n - 2]
    for i in range(1, n - 1):
        Y[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]) / (h[i - 1] + h[i])
    
    S = np.linalg.solve(H, Y)
    print("S =", end = ' ')
    print(S, "\n--------")

    return S

def spline_eval(x, y, x_estimate, diff_x0, diff_xn):
    if x_estimate in x:
       return y[x_estimate.index()]
    n = len(x)
    h = np.diff(x)
    S = cubic_spline_coeff(x, y, diff_x0, diff_xn)
    for i in range(n - 1):
       if x[i] < x_estimate and x_estimate < x[i + 1]:
           res = S[i] * ((x[i + 1] - x_estimate) ** 3) / (6 * h[i]) 
           res += S[i + 1] * ((x_estimate - x[i]) ** 3) / (6 * h[i])
           res += (y[i] - (S[i] * h[i] * h[i]) / 6) * (x[i + 1] - x_estimate) / h[i]
           res += (y[i + 1] - (S[i + 1] * h[i] * h[i]) / 6) * (x_estimate - x[i]) / h[i]
           return res

    return np.inf

# Ex 13
x = np.array([0, 1, 2, 3])
y = np.array([1, 0, -1, 0])

print(spline_eval(x, y, 2.5, 0, -6))