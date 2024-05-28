import numpy as np

def diff(f, x: float, tol: float) -> float:
    return (f(x + tol) - f(x - tol)) / (2 * tol)

def partial_diff(f, x: list, id: int, tol: float) -> float:
    x_plus = x[:]
    x_minus = x[:]
    x_plus[id] += tol
    x_minus[id] -= tol
    return (f(*x_plus) - f(*x_minus)) / (2 * tol)

#Bai toan thuan
def cumulative_error_direct_solver(f, x, x_abs_err, tol: float) -> float:
    if isinstance(x, float):
        x = [x]
        x_abs_err = [x_abs_err]
    res = 0
    for i in range(len(x)):
        res += abs(partial_diff(f, x, i, tol)) * x_abs_err[i]
    return res

#Bai toan nguoc
def cumulative_error_inverse_solver(f, x, y_abs_err, tol: float):
    if isinstance(x, float):
        return y_abs_err / abs(diff(f, x, tol))
    res = []
    for i in range(len(x)):
        res.append(y_abs_err / abs(partial_diff(f, x, i, tol)))
    return res

def f(x, y):
    return x**2 * np.sin(y) + y**3 * np.cos(x)

# Example usage of the functions
x_point = [1.0, 0.5]
tolerance = 0.01
print("Partial derivative with respect to x:", partial_diff(f, x_point, 0, tolerance))
print("Partial derivative with respect to y:", partial_diff(f, x_point, 1, tolerance))

# Error estimation example
x_error = [0.01, 0.01]
print("Cumulative output error:", cumulative_error_direct_solver(f, x_point, x_error, tolerance))

# Inverse problem example
y_abs_err = 0.05
print("Maximum estimated input errors:", cumulative_error_inverse_solver(f, x_point, y_abs_err, tolerance))
