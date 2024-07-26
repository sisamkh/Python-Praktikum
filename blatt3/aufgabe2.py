import numpy as np

def ausgleich_poly(x, y, k):
    # x: array of x-coordinates of the data points
    # y: array of y-coordinates of the data points
    # k: degree of the polynomial

    n = len(x)

    # calculate A
    A = np.vstack([x**i for i in range(k+1)]).T
    print(A)
    # QR decomposition
    #### EYA GIB DEIN FUNKTION HIER
    #######################################
    #######################################
    Q, R = np.linalg.qr(A)
    #######################################
    #######################################
    # calculate Qt * y
    Qt_y = np.dot(Q.T, y)

    # Solve R * beta = Q^T * y for beta
    ##################################################
    ####### Hier brauche ich auch deine Funktion zur zuruck

    beta = np.linalg.solve(R, Qt_y)
    print(beta)
    beta = solve(R, Qt_y)
    print(beta)

    return beta

# solve linear equation containing upper right triangle matrix
def solve(A,b):
    n, _ = A.shape
    x = np.full((n,1),np.nan)
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(n-1,i,-1):
            sum += A[i][j]*x[j]
        x[i] = (b[i] - sum)/A[i][i]
    return x


# Example usage:
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.2, 2.8, 3.6, 4.5, 5.5])
k = 4

# Beispiel
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

beta = ausgleich_poly(x_data, y_data, k)
for i in range(k+1):
    print(f'{beta[i]}x^{k-i}+',end=" ")

print("\n Koeffizienten des Polynoms:", beta)
