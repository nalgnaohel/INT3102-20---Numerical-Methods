import numpy as np
from scipy.linalg import lu_factor, lu_solve, inv

def LU_solve(A : np.array, b : np.array):
    lu, piv = lu_factor(A)
    x = lu_solve((lu, piv), b)
    return x

print("Exercise 3:")
A = np.array([[5, 4, 1], [10, 9, 4], [10, 13, 15]])
b = np.array([6.8, 17.6, 38.4])
#x0 = np.zeros(A.shape[0])
x = LU_solve(A, b)
print(x)
print(np.allclose(np.matmul(A, x) - b, np.zeros(A.shape[0])))
#[0.4 0.8 1.6]
