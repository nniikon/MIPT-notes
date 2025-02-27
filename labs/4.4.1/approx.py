import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * x + b

filename = sys.argv[1]
data = np.loadtxt(filename)
xdata = data[:, 0]
ydata = data[:, 1]

popt, pcov = curve_fit(func, xdata, ydata)

sigma_a, sigma_b = np.sqrt(np.diag(pcov))

print("Approximated constant a =", popt[0])
print("Approximated constant b =", popt[1])
print("sigma a =", sigma_a)
print("sigma b =", sigma_b)

# x_min = min(xdata)
# x_max = max(xdata)

x_min = 0
x_max = max(xdata) + 100

# Generate points for the fitted line
x_fit = np.linspace(x_min, x_max, 100)
y_fit = func(x_fit, *popt)

y_errors = 0.003

plt.errorbar(xdata, ydata, yerr=y_errors, fmt='o', capsize=5)
plt.plot(x_fit, y_fit, 'r-', label = 'МНК')
plt.xlabel(r'$\lambda$, нм')
plt.ylabel(r'sin($\phi$)')
plt.legend()
plt.grid(True)
plt.savefig('fit_result.png')  # Saves the plot to a file
#plt.show()
