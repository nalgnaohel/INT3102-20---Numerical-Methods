import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    
    x = np.copy(x0)
    for it in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new
        x = x_new
    
    raise Exception("Gauss-Seidel method did not converge")

print("Ex 13:")
A = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 1]])
b = np.array([2, 2, 2])
x0 = np.zeros_like(b)
gauss_seidel(A, b, x0, 1e-6, 100)
