import numpy as np 
N=int(input('N='))
M=int(input('M='))

A=np.zeros((N, M))
for i in range(0, N, 1):
    for j in range(0, M, 1):
        if i==0 and j==0:
            A[i, j] = np.sin(N * i + M * j)
        else:
            A[i, j] = np.sin(N * (i+1) + M * (j + 1)) 

for i in range(0, N, 1):
    for j in range(0, M, 1):
        if A[i, j]<0:
            A[i,j]=0
        

print(A)

