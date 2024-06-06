import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk Interpolasi Polinom Lagrange
def lagrange_basis(x_values, k, x):
    """Menghitung basis Lagrange L_k(x)"""
    basis = 1
    for i in range(len(x_values)):
        if i != k:
            basis *= (x - x_values[i]) / (x_values[k] - x_values[i])
    return basis

def lagrange_interpolation(x_values, y_values, x):
    """Menghitung nilai interpolasi Lagrange di x"""
    interpolated_value = 0
    for k in range(len(x_values)):
        interpolated_value += y_values[k] * lagrange_basis(x_values, k, x)
    return interpolated_value

# Membuat plot
x_plot = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_plot]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_lagrange, label='Lagrange Interpolation', color='blue')
plt.scatter(x, y, label='Data Points', color='black')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()