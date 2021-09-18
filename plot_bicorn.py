from sympy import plot_implicit, symbols, Eq, solve
import numpy as np
import matplotlib.pyplot as plt


def get_bicorn_data():
    x, y = symbols("x y")
    a = 1
    expr = y**2 * (a**2-x**2)-(x**2+2*a*y-a**2)**2
    pli = plot_implicit(expr)
    series = pli[0]
    data, action = series.get_points()
    return np.array([(x_int.mid, y_int.mid) for x_int, y_int in data]).T


def get_catenary_data(lines = 100):
    x = np.linspace(-1, 1, lines)
    y = np.cosh(x)
    return np.stack([x, y])


def get_parabola(lines=101):
    x = np.linspace(-1, 1, lines)
    y = x**2 + np.cosh(0)
    return np.stack([x, y])


def get_cissoid_of_diocles(lines=101):
    x = np.linspace(0, 1.999, lines)
    y = np.sqrt(x**3/(2-x))
    return np.stack([np.concatenate([x[::-1], x]),
                     np.concatenate([y[::-1], -y])
                     ])

def get_fermats_spiral(lines=101):
    theta = np.linspace(0, 2*np.pi, lines)
    r = np.sqrt(theta)
    
# data = get_bicorn_data()
# plt.figure()
# plt.plot(data[0], data[1])
# plt.show()

# data = get_catenary_data()
# data_par = get_parabola()
# plt.figure()
# plt.plot(data[0], data[1])
# plt.plot(data_par[0], data_par[1])
# plt.show()

data = get_cissoid_of_diocles()
plt.figure()
plt.plot(data[0], data[1])
plt.show()

