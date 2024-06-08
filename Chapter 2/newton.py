import numpy as np

def f(x: float) -> float:
    return (x - 1) ** 2 + x ** 4

def df(x: float) -> float:
    return 4 * (x ** 3) + 2 * x - 2

def newton(p0 : float, max_iter : int, tol: float):
    i = 0
    while i < max_iter:
        p = p0 - f(p0) / df(p0)
        print(p)
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
    print(" iterations.")

print("Exercise 13:")
newton(2, 1000, 0.0001)
