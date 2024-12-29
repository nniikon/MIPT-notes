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
x = np.linspace(0*min(x_data), 1.31*max(x_data), 100)
plt.plot(x, 0.008*x - 0.5)
ax.errorbar(x_data, y_data, xerr=0.0, yerr=1, fmt='o', capsize=6)
plt.xlabel(r'$\nu$, ${Hz}$')
plt.ylabel(r'$\tan{\psi}$')

plt.show()
