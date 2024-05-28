import numpy as np

def f(x: float) -> float:
    return x - np.cos(x)

def secant(p0 : float, p1 : float, max_iter : int, tol: float):
    i = 1
    while i < max_iter:
        p = p1 - (f(p1) * (p1 - p0)) / (f(p1) - f(p0))
        if (abs(p1 - p) < tol):
            print("Found the solution ", end='')
            print(p, end="")
            print("at iteration ", end="")
            print(i + 1)
            print(f(p))
            return
        p0 = p1
        p1 = p
        i += 1
    print("Failed to find the solution after ", end="")
    print(max_iter, end="")
    print("iterations.")

secant(0, 0.5, 10, 0.0001)
