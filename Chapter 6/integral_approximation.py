import numpy as np

def f(x):
    return np.cos(x) ** 2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        integral += f(a + i * h)
    
    integral *= h
    
    return integral

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    
    integral = 0.0
    
    for i in range(n):
        midpoint = a + (i + 0.5) * h
        integral += f(midpoint)
    
    integral *= h
    
    return integral

def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Number of intervals (n) must be even.")

    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    integral *= h / 3
    
    return integral

a = 0.5  
b = 1
n = 1000 
#x^4
result = trapezoidal_rule(f, a, b, n)
print("Trapezoidal Rule Approximated value of the integral:", result)
result = midpoint_rule(f, a, b, n)
print("Midpoint Rule Approximated value of the integral:", result)
result = simpsons_rule(f, a, b, n)
print("Simpson Rule Approximated value of the integral:", result)

#2 / (x - 4)
a, b  = 0,  0.5
result = trapezoidal_rule(f, a, b, n)
print("Trapezoidal Rule Approximated value of the integral:", result)
result = midpoint_rule(f, a, b, n)
print("Midpoint Rule Approximated value of the integral:", result)
result = simpsons_rule(f, a, b, n)
print("Simpson Rule Approximated value of the integral:", result)

#(cosx)^2
a, b  = -0.25,  0.25
result = trapezoidal_rule(f, a, b, n)
print("Trapezoidal Rule Approximated value of the integral:", result)
result = midpoint_rule(f, a, b, n)
print("Midpoint Rule Approximated value of the integral:", result)
result = simpsons_rule(f, a, b, n)
print("Simpson Rule Approximated value of the integral:", result)