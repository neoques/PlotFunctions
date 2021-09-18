import matplotlib.pyplot as plt
import numpy as np


def cantor(i, x):
    if i == 0:
        return x
    else:
        if x <= 1/3:
            return cantor(i-1, 3 * x)/2
        elif 1/3 < x <= 2/3:
            return cantor(i-1, 1/2)
        else:
            return 1/2+cantor(i-1, 3 * x - 2)/2


fig = plt.figure()
ax = plt.axes()
iterations = 5
lines = 3**iterations + 1
print(lines)
x = np.linspace(0, 1, lines)
y = []
for a_x in x:
    y.append(cantor(iterations, a_x))
plt.plot(x, y)
plt.show()