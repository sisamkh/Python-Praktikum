import numpy as np
A = np.array([[1,2,3,4,5],
             [0,2,3,4,5],
             [0,0,3,4,5],
             [0,0,0,4,5],
             [0,0,0,0,5]])
n = 5
for i in range(n-1,-1,-1):
    sum = 0
    for j in range(n-1,i,-1):
        print(f'({i},{j})',end=" ")
        sum += A[i][j]
    print(sum)
    print("\n")
