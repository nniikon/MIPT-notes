import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([5.398280842, 1.450191379, 0.6605525221, 0.3761938285, 0.2425698337])
y = np.array([6.392556445, 2.213809561, 1.002948846, 0.6303390899, 0.5610954856])

# Error bars
x_err = 0.05 * x  # 5% error in x
y_err = 0.1 * y   # 10% error in y

# Calculate the best fit parameters using the least squares method
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Print the best fit parameters
print(f"Best fit parameters: k = {m}, b = {c}")

# Plotting
plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', capsize=5)

# Plot the best fit line
x_fit = np.linspace(min(x), max(x), 100)
y_fit = m * x_fit + c

plt.plot(x_fit, y_fit, color='red')
plt.xlabel('$1/R^2 * 10^6$')
plt.ylabel('$1/\\theta^2$')
plt.legend()
plt.grid(True)
plt.show()
