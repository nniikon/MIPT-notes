import matplotlib.pyplot as plt
import numpy as np

# Data for "R = 2000"
nu_nu0_2000 = [0.63, 0.66, 0.69, 0.73, 0.76, 0.79, 0.82, 0.85, 0.89, 0.92, 0.95, 0.98, 1.00, 1.16, 1.32, 1.48, 1.65, 1.81, 1.97, 2.13, 2.29, 2.45, 2.61, 2.77, 2.94]
U_U0_2000 = [0.40, 0.45, 0.50, 0.56, 0.63, 0.69, 0.76, 0.83, 0.89, 0.93, 0.97, 1.00, 1.00, 0.94, 0.82, 0.74, 0.68, 0.64, 0.62, 0.60, 0.57, 0.56, 0.55, 0.54, 0.54]

# Data for "R = 400"
nu_nu0_400 = [0.87, 0.89, 0.91, 0.92, 0.94, 0.96, 0.97, 0.99, 1.00, 1.01, 1.03, 1.04, 1.06, 1.08, 1.09, 1.11, 1.13, 1.14, 1.16, 1.18, 1.19]
U_U0_400 = [0.40, 0.45, 0.51, 0.61, 0.71, 0.81, 0.94, 0.99, 1.00, 1.00, 0.94, 0.84, 0.76, 0.68, 0.62, 0.56, 0.52, 0.48, 0.45, 0.43, 0.40]

# Plotting the data
plt.figure(figsize=(8, 6))

yerr_2000 = np.full_like(U_U0_2000, 0.02)
yerr_400  = np.full_like(U_U0_400,  0.02)

# Plot for "R = 2000" with blue color
plt.errorbar(nu_nu0_2000, U_U0_2000, marker='o', yerr=yerr_2000, color='blue', label='R = 2000 Ом', linestyle='-', linewidth=2, capsize=5)

# Plot for "R = 400" with orange color
plt.errorbar(nu_nu0_400, U_U0_400, marker='o', yerr=yerr_400, color='orange', label='R = 400 Ом', linestyle='-', linewidth=2, capsize=5)

# Adding labels and title
plt.xlabel(r'$\nu / \nu_0$', fontsize=14)
plt.ylabel(r'$U / U_0$', fontsize=14)
plt.title('АЧХ', fontsize=16)

# Adding a legend
plt.legend()

# Display the grid
plt.grid(True)

# Show the plot
plt.show()
