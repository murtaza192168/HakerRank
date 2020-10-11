import numpy as np

N,M = map(int,input().split())

A,B=(np.array([input().strip().split() for i in range(N)],dtype=int)for i in range(2))
print(A+B , A-B , A*B ,A//B , A%B , A**B , sep='\n')
