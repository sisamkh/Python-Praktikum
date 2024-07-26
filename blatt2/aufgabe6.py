# Gruppe 3
# Sisam Khanal
# Eya Rouissi
# Vladimir Suschevici

import numpy as np
import math

def cholesky(mat):
    m,n = mat.shape
    if m != n:                                 #Prüfung, ob Matrix quadratisch
       return False

    for i in range(m):                         #Prüfung, ob Matrix symmetrisch
       for k in range(n):
          if mat[i][k] != mat[k][i]:
             return False

    L = np.zeros((m,n))                         #Initialisierung von L

    L[0,0] = math.sqrt(mat[0,0])                #Berechnung des ersten Wertes der Diagonale von L

    L[1:m,0] = 1.0/L[0,0] * mat[1:m,0]          #Berechnung der ersten Spalte von L (untenliegende Werte nach L(0,0))

    for i in range(1,m):
        for k in range(1,n):

         L[k][k] = math.sqrt(mat[k][k] - L[k][1:k-1]*L[k][1:k-1])                                   #Berechnung der Diagonale von L

         L[i][k] = 1.0/L[k][k] * math.sqrt(mat[i][k] - np.dot(L[i][1:k-1],L[i][1:k-1].transpose())) #Berechnung der jeweiligen Spalte unterhalb des Diagonalwertes

    if np.dot(L,np.transpose(L)) != mat:        #Prüfung, ob Cholesky-Zerlegung eindeutig
       return False

    return print(np.matrix(L))

# A = np.array([[3.0, 1.0, 1.0],
#               [1.0, 1.0, 3.0],
#               [1.0, 3.0, 1.0]])
# print(cholesky(A))
