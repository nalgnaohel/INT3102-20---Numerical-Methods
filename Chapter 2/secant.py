import numpy as np

def f(x: float) -> float:
    return x ** 2 - 6

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
        print(p0, " ", p1, " ", p)
        i += 1
    print("Failed to find the solution after ", end="")
    print(max_iter, end="")
    print("iterations.")

print("Exercise 3a:")
secant(3, 2, 3, 0.00001)
#2.4545454545454546
