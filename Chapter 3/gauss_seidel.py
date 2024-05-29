import numpy as np

def row_swap(A: np.array, org: int, tar: int):
    temp = A[org].copy()
    A[org] = A[tar]
    A[tar] = temp

def gauss_seidel(A: np.array, b: np.array, x0: np.array, max_iter: int, tol : float):
    iter = 0
    n = x0.shape[0]
    x = np.zeros(n)
    for i in range(n):
        if A[i][i] == 0:
            swapped = False
            for j in range(n):
                if A[j][i] != 0 and A[i][j] != 0:
                    row_swap(A, i, j)
                    row_swap(b, i, j)
                    swapped = True
                    break
            if swapped == False:
                print("Cannot apply Jacobi method.")
                return

    while iter < max_iter:
        for i in range(n):
            temp = b[i]
            for j in range(i):
                temp -= A[i][j] * x[j]
            for j in range(i + 1, n, 1):
                temp -= A[i][j] * x0[j]
            x[i] = temp / A[i][i]
        if (np.linalg.norm(x - x0, ord = np.inf) < tol):
            print("Found the solution.", end = ' ')
            print(x)
            return
        x0 = x.copy()
        print(iter + 1, end = ": ")
        print(x)
        iter += 1
    print("End of the process.")

A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([1, 1, 1])
x0 = np.zeros(A.shape[0])
jacobi(A, b, x0, 150, 1e-6)
# [0.35714275 0.42857137 0.35714284]
# print(A)