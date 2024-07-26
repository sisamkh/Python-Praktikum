# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici

import numpy as np
import math
def spectral_norm(A, max_iter: int = 1000000): # mit power iteration
    if not A.any(): #falls das ein 0 Matrix oder Vektor ist
        return 0.0
    b_k = np.random.rand(A.shape[0])  # nimm einen beliebigen Vektor
    A = np.dot(A, np.transpose(A))
    for _ in range(max_iter):
        # berechne Ab
        Ab = np.dot(A, b_k)

        # brechne den Norm von Ab
        b_k1_norm = np.linalg.norm(Ab)

        # normiere b_k1
        b_k1 = Ab / b_k1_norm

        # pruefe fuer Konvergenz
        if np.linalg.norm(b_k1 - b_k) < 1e-16:
            break
        b_k = b_k1
    return math.sqrt(b_k1_norm)

def zeilensummennorm(A):
    n, _ = A.shape
    summen = []
    for i in range(n):
        summen.append(A[i].sum())
    return max(summen)

def konditionszahl(A):
    snormA = spectral_norm(A)
    try:
        Ainv = np.linalg.inv(A)
    except:
        return np.inf
    snormAinv = spectral_norm(Ainv)
    return snormA * snormAinv

def qualität(A,b,x_tilde):
    r = np.dot(A, x_tilde) - b
    kon_A = konditionszahl(A)
    A_norm = spectral_norm(A)
    r_norm = spectral_norm(r)
    return kon_A * r_norm / A_norm

def lösen(A,b):
    if not A.any():
        print("Sie haben null Matrix eingegeben. ")
        return
    if ist_symm(A):
        # Cholesky Zerlegung
        pass
    else:
        # LR Zerlegung
        pass

def ist_symm(A):
    for i in A.shape[0]:
        for j in A.shape[1]:
            if not A[i][j] == A[j][i]:
                return False
    return True


# da wir Aufgaben separat gemacht haben, hatte ich kein Algo für die
# LR und Cholesky Zerlegung
# A = np.array([[3,2],[-2,0]])
# x = np.array([[1],[2]])
# b = np.array([[7],[-2]])
# print(qualitat(A,b,x))
