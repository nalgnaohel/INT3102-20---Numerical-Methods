import numpy as np
import matplotlib.pyplot as plt

def dfx(x: float, y: float, quest):
    if quest == "a":
        return y /x - (y / x) ** 2
    elif quest == "b":
        return 1 + y/x + (y/x) ** 2
    elif quest == "c":
        return -1 * (y + 1) * (y + 3)
    return -5 * y + 5 * (x ** 2) + 2 * x

def ddfx(x: float, y: float, quest):
    return (dfx(x, y, quest) * x - y) / (x ** 2)

def actual(x, quest):
    if quest == "a":
        return x / (1 + np.log(x))
    elif quest == "b":
        return x * np.tan(np.log(x))
    elif quest == "c":
        f = x.copy()
        for i in range(len(x)):
            f[i] = np.exp(-2 * x[i])
        return 2 / (1 + np.exp(f)) - 3
    f = x.copy()
    for i in range(len(x)):
        f[i] *= x[i]
        x[i] = np.exp(-5 * x[i])
        x[i] /= 3
        x[i] += f[i]
    return x 

def taylor_method(x0: float, y0: float, h: float, max_iter: int, quest):
    #order 2
    #y_(i + 1) = y_i + h * dfx + (h ** 2 / 2) * ddfx
    x, y = [], []
    x.append(x0)
    y.append(y0)
    for i in range(max_iter):
        y0 = y0 + h * dfx(x0, y0, quest) + (h ** 2 / 2) * ddfx(x0, y0, quest)
        x0 += h
        x.append(x0)
        y.append(y0)
    return x, y

def midpoint_method(x0: float, y0:float, h: float, max_iter: int, quest):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        y_mid = y + h / 2 * dfx(x0, y0, quest)
        x_mid = x + h / 2
        y = y + h * dfx(x_mid, y_mid, quest)
        x = x_mid + h / 2
        xl.append(x)
        yl.append(y)
    return xl, yl   

def heun_method(x0: float, y0: float, h: float, x_end: float, quest):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    while x < x_end:
        y_pred = y + h * dfx(x, y, quest)
        y = y + (h / 2) * (dfx(x, y, quest) + dfx(x + h, y_pred, quest))
        x += h
        x = np.round(x, decimals=4)
        xl.append(x)
        yl.append(y)
    return xl, yl

def runge_kutta_method(x0: float, y0: float, h: float, x_end: float, quest):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    while x < x_end:
        k1 = dfx(x, y, quest)
        k2 = dfx(x + 0.5 * h, y + 0.5 * k1 * h, quest)
        k3 = dfx(x + 0.5 * h, y + 0.5 * k2 * h, quest)
        k4 = dfx(x + h, y + k3 * h, quest)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        x = np.round(x, decimals=4)
        xl.append(x)
        yl.append(y)

    return xl, yl

# print("Taylor method:") (Ex 3)
# for i in range(2):
#     print(taylor_method(1, 2, 0.25, 5)[i])
# print("--------------------")
#[1, 1.25, 1.5, 1.75, 2.0, 2.25]
#[2, 2.78125, 3.6125, 4.485416666666667, 5.394047619047619, 6.333928571428571]

a = [1, 1, 0, 0]
b = [1, 0, -2, 1/3]
h = [0.1, 0.2, 0.2, 0.1]
x_end = [2, 3, 2, 1]
q = ["a", "b", "c", "d"]
#Sample with Heun and R4, Ex 3 - Heun
print("--------------------")
print("Heun method:")
for i in range(4):
    x, y = heun_method(a[i], b[i], h[i], x_end[i], q[i])
    x_act = x.copy()
    y_act = actual(x_act, q[i])
    print(x_act, y_act)
    plt.figure()
    plt.plot(x, y, 'o-', label='Heun')
    plt.plot(x_act, y_act, '-', label='Actual Solution')
    plt.title(f'Problem {q[i]})')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.legend()
    plt.grid(True)
    plt.show()
         
#Ex 13
print("--------------------")
print("Runge-Kutta method:")
for i in range(4):
    x, y = runge_kutta_method(a[i], b[i], h[i], x_end[i], q[i])
    x_act = x.copy()
    y_act = actual(x_act, q[i])
    print(x_act, y_act)
    plt.figure()
    plt.plot(x, y, 'o-', label='RK4')
    plt.plot(x_act, y_act, '-', label='Actual Solution')
    plt.title(f'Problem {q[i]})')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.legend()
    plt.grid(True)
    plt.show()
print("--------------------")