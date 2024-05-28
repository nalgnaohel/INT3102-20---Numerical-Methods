import numpy as np

def g(x : float) -> float:
    return np.sqrt((x + 3) / (x ** 2 + 2))

def fixed_point(p0, max_iter : int, tol : float) -> float:
    i = 0
    while (i < max_iter):
        p = g(p0)
        print(p0, end = ' ')
        print(p)
        if (abs(p - p0) < tol):
            print("Found the solution: ", end = "")
            print(p, end = " ")
            print("at iteration ", end="")
            print(i + 1)
            return p
        p0 = p
        i += 1
    print("Failed to find the solution after ", end ="")
    print(max_iter, end =  ' ')
    print("solution.")
    return np.inf

fixed_point(1, 3, 0.01)
