# Gruppe 3
# Eya Rouissi(1913192)
# Sisam Khanal (2312802)
# Vladimir Suschevici(1732301)

import numpy as np

def my_lu(a):
    n = len(a)
    l = np.zeros((n, n))
    u = np.zeros((n, n))
    
    for j in range(n):
        l[j][j] = 1
        for k in range(j, n):
            u[j][k] = a[j][k]
        for i in range(j + 1, n):
            l[i][j] = a[i][j] / u[j][j]
            for k in range(j + 1, n):
                a[i][k] = a[i][k] - l[i][j] * u[j][k]
    return l, u

def choose_pivot_strategy():
    while True:
        strategy = input("Choose pivot strategy (none/partial/full): ").lower()
        if strategy in ['none', 'partial', 'full']:
            return strategy
        else:
            print("Invalid strategy. Please choose 'none', 'partial', or 'full'.")

def partial_pivot_lu(A):
    n = A.shape[0]
    # Initialize permutation matrix P as an identity matrix
    P = np.eye(n)
    # Initialize lower triangular matrix L and upper triangular matrix U
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    # Make a copy of A to use for factorization
    U = A.copy()
    
    for i in range(n):
        # Partial pivoting
        pivot = np.argmax(abs(U[i:n, i])) + i
        # Swap rows in U
        U[[i, pivot], i:n] = U[[pivot, i], i:n]
        # Swap rows in P
        P[[i, pivot], :] = P[[pivot, i], :]
        # Swap rows in L
        L[[i, pivot], :i] = L[[pivot, i], :i]

        # Ensure the matrix is not singular
        if abs(U[i, i]) < 1e-12:
            raise ValueError("Matrix is singular!")

        # Decompose into L and U matrices
        for j in range(i+1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:n] = U[j, i:n] - L[j, i] * U[i, i:n]

    # Set the diagonal elements of L to 1
    np.fill_diagonal(L, 1)
    
    return L, U, P

def full_pivot_lu(A):
    n = A.shape[0]
    # Initialize permutation matrices P and Q as identity matrices
    P = np.eye(n)
    Q = np.eye(n)
    # Initialize lower triangular matrix L and upper triangular matrix U
    L = np.zeros_like(A)
    U = np.copy(A)

    for k in range(n):
        # Full pivoting: find the indices of the maximum element in the remaining submatrix
        i, j = divmod(np.argmax(np.abs(U[k:, k:])), n-k)
        i += k
        j += k

        # Swap rows and columns according to the pivots
        U[[k, i], :] = U[[i, k], :]
        P[[k, i], :] = P[[i, k], :]
        U[:, [k, j]] = U[:, [j, k]]
        Q[:, [k, j]] = Q[:, [j, k]]

        # Adjust L matrix for row swapping and ensure column pivots are accounted for prior steps
        L[[k, i], :k] = L[[i, k], :k]
        L[:, [k, j]] = L[:, [j, k]]

        # LU Decomposition using Gaussian elimination
        for i in range(k+1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] = U[i, k:] - L[i, k] * U[k, k:]

    # Set the diagonal elements of L to 1
    np.fill_diagonal(L, 1)

    return P, L, U, Q


def loesung(a, choose_pivot_strategy=None):
    if choose_pivot_strategy is None:
        return my_lu(a)
    elif choose_pivot_strategy == 'partial':
        return partial_pivot_lu(a)
    elif choose_pivot_strategy == 'full':
        return full_pivot_lu(a)
    else:
        raise ValueError("Invalid pivot strategy. Please choose 'None', 'partial', or 'full'.")

# Test
# A = np.array([[3.0, 1.0, 6.0], [2.0, 1.0, 3.0], [1.0, 1.0, 1.0]])

# print("No Pivot LU Decomposition:")
# L_no_pivot, R_no_pivot = my_lu(A)
# print("L:")
# print(L_no_pivot)
# print("R:")
# print(R_no_pivot)
# print("Reconstructed matrix A:")
# print(np.matmul(L_no_pivot, R_no_pivot))
# A = np.array([[3.0, 1.0, 6.0], [2.0, 1.0, 3.0], [1.0, 1.0, 1.0]])
# print("\nPartial Pivot LU Decomposition:")
# L_partial, R_partial, P_partial = partial_pivot_lu(A)
# print("L:")
# print(L_partial)
# print("R:")
# print(R_partial)
# print("P:")
# print(P_partial)
# print("Reconstructed matrix A:")
# print(np.matmul(P_partial, np.matmul(L_partial, R_partial) ))
# A = np.array([[3.0, 1.0, 6.0], [2.0, 1.0, 3.0], [1.0, 1.0, 1.0]])
# print("\nFull Pivot LU Decomposition:")
# P_full, L_full, U_full, Q_full = full_pivot_lu(A)
# print("L:")
# print(L_full)
# print("R:")
# print(U_full)
# print("P:")
# print(P_full)
# print("Reconstructed matrix A:")
# print(np.matmul(np.matmul(P_full, np.matmul(L_full, U_full)),Q_full))
