import numpy as np

# mat = np.array([[1,2,3],
#                 [2,3,4],
#                 [3,4,5]])

# def cor(mat,i,j):
#     return mat[i-1][j-1]
# def setze(mat, i, j, x):
#     mat[i-1][j-1] = x
a = np.array([[3.0,1.0,0.0],
              [2.0,1.0,3.0],
              [0.0,1.0,1.0]])
l = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
r = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
n = len(a)
for j in range(n):
    l[j][j] = 1
    for k in range(j,n):
        r[j][k] = a[j][k]
    for i in range(j+1,n):
        l[i][j] = a[i][j]/r[j][j]
        for k in range(j+1, n):
            a[i][k] = a[i][k] - l[i][j]*r[j][k]

print(l,"\n",r)
print(np.matmul(l,r))