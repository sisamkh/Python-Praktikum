# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici

import math
import numpy as np
import scipy as sp

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

def jacobi_matrix(F,x_, epsilon = 1e-8):
    x = x_
    n = len(x)
    jacobi = np.zeros((n,n))
    for j in range(n):
        ejej = np.zeros(n)
        # definiere epsilon_j e_j
        ejej[j] = epsilon
        # berechne den zähler
        dF = F(x+ ejej) - F(x)
        jacobi[:, j] = dF/epsilon

    return jacobi


def newton_verfahren(F,x,TOL):
    iteration = 0
    while True:
        iteration += 1
        F_x = F(x)
        j_x = jacobi_matrix(F,x)
        delta = np.linalg.solve(j_x, -F_x)
        x = x + delta
        if (np.linalg.norm(delta) < TOL):
            return x, iteration

def vereinfach_newton(F,x,TOL):
    j_x = jacobi_matrix(F,x)
    L,R =lr_zerlegung(j_x)
    print(np.allclose(j_x, L @R))
    iteration = 0
    while True:
        iteration += 1
        y = np.linalg.solve( L, -F(x))
        delta = np.linalg.solve(R,y)
        x = x + delta
        if (np.linalg.norm(delta) < TOL):
            return x, iteration

def F(x):
    return np.array([x[1] - math.log(x[0]),
                    (x[1]+1)**2 - (x[0]-0.5)**2])

x = np.array([1.0,0.0])

nullstell = newton_verfahren(F,x,1e-8)
print(nullstell)
print(x)
nullstl = vereinfach_newton(F,x,1e-8)
print(nullstl)
