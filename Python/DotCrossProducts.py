import numpy as np
N=int(input())
A=np.array([input().split() for i in range(N)],int)
B = np.array([input().split() for i in range(N)],int)

multiplication = np.dot(A,B)
print(multiplication)