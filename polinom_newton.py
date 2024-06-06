import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def newton_divided_differences(x_values, y_values):
    n = len(x_values)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y_values
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x_values[i + j] - x_values[i])
    
    return divided_diff

# Fungsi untuk Interpolasi Polinom Newton
def newton_interpolation(x_values, y_values, x):
    divided_diff = newton_divided_differences(x_values, y_values)
    n = len(x_values)
    interpolated_value = divided_diff[0, 0]  # Awali dengan nilai pertama
    product_term = 1.0  # Inisialisasi produk
    
    for k in range(1, n):
        product_term *= (x - x_values[k - 1])
        interpolated_value += divided_diff[0, k] * product_term
    
    return interpolated_value

# Membuat plot untuk hasil interpolasi Newton
x_plot = np.linspace(5, 40, 400)
y_newton = [newton_interpolation(x, y, xi) for xi in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_newton, label='Newton Interpolation', color='red')
plt.scatter(x, y, label='Data Points', color='black')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()