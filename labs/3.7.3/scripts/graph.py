import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()
x_data = []
y_data = []
for line in lines:
    x, y = map(float, line.split())
    x_data.append(x)
    y_data.append(y)


fig, ax = plt.subplots()
x = np.linspace(0.99*min(x_data), 1.01*max(x_data), 100)
plt.plot(x, 2.559573 * 10**(-18)*x)
ax.errorbar(x_data, y_data, xerr=0.0, yerr=0.0000001, fmt='o', capsize=6)
plt.xlabel(r'$\nu^{3/2}, s^{3/2}$')
plt.ylabel(r'$ak, {cm}^{-2}$')

plt.show()
