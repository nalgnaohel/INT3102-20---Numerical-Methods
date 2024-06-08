import numpy as np

def f(x: float):
    return x ** 3 - 25

def bisection(a : float, b : float, tol : float):
    n_bound = np.log2((b - a) / tol)
    i = 0
    #print("Maximum number of iterations:", end = " ")
    #print(n_bound)
    while i < n_bound:
        mid = a + (b - a) / 2
        # print("Iteration", end = " ")
        # print(i + 1, end = "")
        # print(":", end = ' ')
        # print(a, end = ' ')
        # print(b, end = ' ')
        # print(mid)
        if (f(mid) == 0 or (b - a) / 2 < tol):
            # print("Found the solution. The solution is", end = ' ')
            # print(mid)
            return mid
        if (f(a) * f(mid) > 0):
            a = mid
        else:
            b = mid
        i += 1
    # print("Found the solution. The solution is", end = ' ')
    # print(mid)
    return mid
    
#Exercise 3 - Bisection Method
print("Exercise 3:")
print("a. [0, 1]: ", bisection(0, 1, 0.01))
print("b. [1, 3.2]: ", bisection(1, 3.2, 0.01))
print("c. [3.2, 4]: ", bisection(3.2, 4, 0.01))
print("-----------")
'''
a. [0, 1]:  0.9921875
b. [1, 3.2]:  3.19140625
c. [3.2, 4]:  3.99375
'''

#Exercise 13 - Bisection Method
print("Exercise 13:")
print("Approximation: ", bisection(2, 3, 0.0001)) #2.92401123046875
