import numpy as np

def dfx(x: float, y: float):
    return 1 + x ** 2 + y

def ddfx(x: float, y: float):
    return 2 * x + dfx(x, y)

def taylor_method(x0: float, y0: float, h: float, max_iter: int):
    #order 2
    #y_(i + 1) = y_i + h * dfx + (h ** 2 / 2) * ddfx
    x, y = [], []
    x.append(x0)
    y.append(y0)
    for i in range(max_iter):
        y0 = y0 + h * dfx(x0, y0) + (h ** 2 / 2) * ddfx(x0, y0)
        x0 += h
        x.append(x0)
        y.append(y0)
    return x, y

def midpoint_method(x0: float, y0:float, h: float, max_iter: int):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        y_mid = y + h / 2 * dfx(x0, y0)
        x_mid = x + h / 2
        y = y + h * dfx(x_mid, y_mid)
        x = x_mid + h / 2
        xl.append(x)
        yl.append(y)
    return xl, yl   

def heun_method(x0: float, y0: float, h: float, max_iter: int):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        y_pred = y + h * dfx(x, y)
        y = y + (h / 2) * (dfx(x, y) + dfx(x + h, y_pred))
        x += h
        xl.append(x)
        yl.append(y)
    return xl, yl

def runge_kutta_method(x0: float, y0: float, h: float, max_iter: int):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        k1 = dfx(x, y)
        k2 = dfx(x + 0.5 * h, y + 0.5 * k1 * h)
        k3 = dfx(x + 0.5 * h, y + 0.5 * k2 * h)
        k4 = dfx(x + h, y + k3 * h)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xl.append(x)
        yl.append(y)

    return xl, yl

print("Euler method:")
for i in range(2):
    print(taylor_method(0, 1, 0.1, 5)[i])
print("--------------------")
print("Midpoint method:")
for i in range(2):
    print(midpoint_method(0, 1, 0.1, 5)[i])
print("--------------------")
print("Heun method:")
for i in range(2):
    print(heun_method(0, 1, 0.1, 5)[i])
print("--------------------")
print("Runge-Kutta method:")
for i in range(2):
    print(runge_kutta_method(0, 0.5, 0.2, 5)[i])
print("--------------------")