import numpy as np

def f(x: float) -> float:
    return x ** 2 - 6

def false_position(p0 : float, p1 : float, max_iter : int, tol: float):
    i = 1
    while i < max_iter:
        p = p1 - (f(p1) * (p1 - p0)) / (f(p1) - f(p0))
        print(p0, end=' ')
        print(p1, end=' ')
        print(p)
        if (abs(p1 - p) < tol):
            print("Found the solution ", end='')
            print(p, end="")
            print("at iteration ", end="")
            print(i + 1)
            print(f(p))
            return
        if (f(p) * f(p1) < 0):
            p0 = p1
        else:
            p1 = p
        i += 1
    print("Failed to find the solution after ", end="")
    print(max_iter, end=" ")
    print("iterations.")

#Exercise 3
print("Exercise 3b:")
print(false_position(3, 2, 3, 10 ** (-5)))
#2.44444444444444