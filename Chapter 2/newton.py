import numpy as np

def f(x: float) -> float:
    return x - np.cos(x)

def df(x: float) -> float:
    return 1 + np.sin(x)

def newton(p0 : float, max_iter : int, tol: float):
    i = 0
    while i < max_iter:
        p = p0 - f(p0) / df(p0)
        if abs(p - p0) < tol:
            print("Found the solution ", end='')
            print(p, end="")
            print("at iteration ", end="")
            print(i + 1)
            #print(f(p))
            return
        p0 = p
        i += 1
    print("Failed to find the solution after ", end="")
    print(max_iter, end="")
    print("iterations.")

newton(0, 10, 0.0001)
