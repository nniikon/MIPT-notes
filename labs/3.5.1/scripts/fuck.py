import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def tanh_function(x, A, B):
    return A * np.tanh(B * x)

def read_file(filename):
    x, y = [], []
    with open(filename, 'r') as f:
        for line in f:
            values = line.strip().split()
            if len(values) == 2:
                x.append(float(values[0]))
                y.append(float(values[1]))
    return np.array(x), np.array(y)

def fit_and_plot(ax, x, y, color, label):
    popt, _ = curve_fit(tanh_function, x, y)
    A, B = popt
    
    # Calculate Mean Squared Error
    y_pred = tanh_function(x, A, B)
    mse = np.mean((y - y_pred)**2)
    
    # Plot scatter and fitted curve
    ax.scatter(x, y, c=color, label=f'{label}')
    x_smooth = np.linspace(min(x), max(x), 200)
    ax.plot(x_smooth, tanh_function(x_smooth, A, B), c=color, linestyle='--', 
            label=f'{label} (Fit): {A:.4f} * tanh({B:.4f}x)')
    
    return A, B, mse

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py file1.txt file2.txt file3.txt")
        sys.exit(1)

    files = sys.argv[1:]
    colors = ['red', 'green', 'blue']
    
    fig, ax = plt.subplots(figsize=(12, 8))

    all_x, all_y = [], []
    for i, (file, color) in enumerate(zip(files, colors)):
        x, y = read_file(file)
        all_x.extend(x)
        all_y.extend(y)
        
        A, B, mse = fit_and_plot(ax, x, y, color, f'{i+2}мА')
        print(f"{i+2}мА: I = {A:.4f} * tanh({B:.6f} * U), MSE = {mse:.6f}")

    ax.legend()
    ax.set_title('ВАХ двойного зонда')
    ax.set_xlabel('U, В')
    ax.set_ylabel('I, мкА')

    # Set x and y axis limits with a bit of padding
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    x_padding = (x_max - x_min) * 0.1
    y_padding = (y_max - y_min) * 0.1
    ax.set_xlim(x_min - x_padding, x_max + x_padding)
    ax.set_ylim(y_min - y_padding, y_max + y_padding)

    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)

    # Customize tick marks
    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.tick_params(axis='both', which='minor', labelsize=6)

    # Add minor ticks
    ax.xaxis.set_minor_locator(plt.AutoLocator())
    ax.yaxis.set_minor_locator(plt.AutoLocator())

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
