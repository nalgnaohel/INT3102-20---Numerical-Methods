import numpy as np

def f(x: float):
    return np.sqrt(x) - 3

def bisection(a : float, b : float, tol : float):
    n_bound = np.log2((b - a) / tol)
    i = 0
    print("Maximum number of iterations:", end = " ")
    print(n_bound)
    while i < n_bound:
        mid = a + (b - a) / 2
        print("Iteration", end = " ")
        print(i + 1, end = "")
        print(":", end = ' ')
        print(a, end = ' ')
        print(b, end = ' ')
        print(mid)
        if (f(mid) == 0 or (b - a) / 2 < tol):
            print("Found the solution. The solution is", end = ' ')
            print(mid)
            return mid
        if (f(a) * f(mid) > 0):
            a = mid
        else:
            b = mid
        i += 1
    print("Found the solution. The solution is", end = ' ')
    print(mid)
    return mid
    
bisection(0, 2, 0.0001)