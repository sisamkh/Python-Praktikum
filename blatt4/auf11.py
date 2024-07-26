# Gruppe 3
# Eya Rouissi(1913192)
# Sisam Khanal (2312802)
# Vladimir Suschevici(1732301)

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Original function
def f(x):
    return 1 / (1 + x**2)

# Function to generate Chebyshev nodes
def chebyshev_nodes(a, b, N):
    k = np.arange(1, N+1)
    nodes = 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2*k - 1) * np.pi / (2 * N))
    return nodes

# Lagrange basis polynomial using sympy
def lagrange_basis(x, x_points, i):
    basis = 1
    for j in range(len(x_points)):
        if j != i:
            basis *= (x - x_points[j]) / (x_points[i] - x_points[j])
    return basis

# Lagrange interpolation polynomial using sympy
def lagrange_interpol(x, x_points, y_points):
    result = 0
    for i in range(len(x_points)):
        result += y_points[i] * lagrange_basis(x, x_points, i)
    return result

# Function to print Lagrange interpolation polynomial in a readable format using sympy
def print_lagrange_polynomial(x_points, y_points):
    x = sp.symbols('x')
    polynomial = 0
    for i in range(len(x_points)):
        L_i = lagrange_basis(x, x_points, i)
        polynomial += y_points[i] * L_i
    polynomial = sp.expand(polynomial)
    print("Lagrange Interpolation Polynomial L(x):")
    print(polynomial)
    print()

# Plot function and its Lagrange interpolation
def plot_lagrange_interpolation(N_values):
    x_real = np.linspace(-5, 5, 400)
    y_real = f(x_real)

    plt.figure(figsize=(14, 10))

    for N in N_values:
        # Generate Chebyshev nodes
        x_points = chebyshev_nodes(-5, 5, N)
        y_points = f(x_points)

        print_lagrange_polynomial(x_points, y_points)

        y_interpol = [lagrange_interpol(x, x_points, y_points) for x in x_real]

        plt.plot(x_real, y_interpol, label=f'N={N}')

    plt.plot(x_real, y_real, 'k', label='f(x) = 1/(1 + x^2)', linewidth=2)
    plt.title('Lagrange Interpolation of f(x) = 1/(1 + x^2)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# List of N values
N_values = [10, 20, 30, 40, 50, 60, 70]
plot_lagrange_interpolation(N_values)
