import numpy as np
from scipy.linalg import lu_factor, lu_solve, inv

def LU_solve(A : np.array, b : np.array):
    lu, piv = lu_factor(A)
    x = lu_solve((lu, piv), b)
    return x


A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([1, 1, 1])
#x0 = np.zeros(A.shape[0])
x = LU_solve(A, b)
print(x)
print(np.allclose(np.matmul(A, x) - b, np.zeros(A.shape[0])))
#[0.35714286 0.42857143 0.35714286]
