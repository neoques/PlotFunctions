import numpy as np
import matplotlib.pyplot as plt

def plot_p_norm(p, lines = 121):
    theta = np.linspace(0, 1, lines)
    x = np.real(np.exp(2 * np.pi * theta * 1j))
    y = np.imag(np.exp(2 * np.pi * theta * 1j))
    r = np.linalg.norm(np.stack([x,y]).T, ord=p, axis=1)
    x, y = x/r, y/r
    return x, y



fig = plt.figure()
ax = plt.axes()
for p in [1, 1.4, 2, 3.4, np.inf]:
    x, y = plot_p_norm(p)
    plt.plot(x, y)

fig = plt.figure()
ax = plt.axes()
for p in [.1, .35, .5, .75, 1]:
    x, y = plot_p_norm(p)
    plt.plot(x, y)

plt.show()