# def vereinfach_newton(F,x,TOL):
#     j_x = jacobi_matrix(F,x)
#     _, L,R = sp.linalg.lu(j_x)
#     iteration = 0
#     while True:
#         iteration += 1
#         y = np.linalg.solve(L, -F(x))
#         delta = np.linalg.solve(R,y)
#         x = x + delta
#         if (np.linalg.norm(delta) < TOL):
#             return x, iteration

import numpy as np
from scipy.linalg import lu

# Define a square matrix
A = np.array([[4, 3], [6, 3]])

# Perform LU decomposition
def lr_zerlegung(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for k in range(i, n):
            U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))

        for k in range(i, n):
            if i == k:
                L[i, i] = 1
            else:
                L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i] for j in range(i))) / U[i, i]

    return L, U
