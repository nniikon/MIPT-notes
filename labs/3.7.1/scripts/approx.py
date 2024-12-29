import numpy as np
import sys
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
print("sigm a =", sigma_a)
print("sigm b =", sigma_b)
