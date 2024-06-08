import numpy as np

def g(x : float, quest: str) -> float:
    if quest == "a":
        return (21 / (x ** 2) + 20 * x) / 21
    elif quest == "b":
        return x - (x ** 3 - 21) / (3 * (x ** 2))
    elif quest == "c":
        return x - (x ** 4 - 21 * x) / (x ** 2 - 21)
    return (21 / x) ** 0.5 

def fixed_point(p0, max_iter : int, tol : float, quest: str) -> float:
    i = 0
    while (i < max_iter):
        p = g(p0, quest)
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

q = ["a", "b", "c", "d"]
print("Exercise 3:")
for i in range(len(q)):
    print(q[i], ":")
    print(fixed_point(1, 1000, 0.0001, q[i]))
    print("----------")
#a: 46, b: 8, c: 2, d: 17