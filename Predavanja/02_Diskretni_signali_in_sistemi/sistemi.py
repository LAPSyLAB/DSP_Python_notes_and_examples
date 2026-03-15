import numpy as np

def sistem1(x):
    y = []
    for n in range(len(x)):
        x_n   = x[n]
        x_n1  = x[n-1] if n-1 >= 0 else 0
        x_n2  = x[n-2] if n-2 >= 0 else 0
        y.append((x_n + x_n1 + x_n2) / 3)
    return np.array(y)

def sistem2(x):
    y = []
    y_prev = 0
    for n in range(len(x)):
        y_n = x[n] + 0.7 * y_prev
        y.append(y_n)
        y_prev = y_n
    return np.array(y)

def sistem3(x):
    y = []
    for n in range(len(x)):
        y.append(n*x[n])
    return np.array(y)