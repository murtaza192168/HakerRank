import numpy as np
A=np.array(input().strip().split(),int)
B=np.array(input().strip().split(),int)

inProduct=np.inner(A,B)
print(inProduct)
outProduct=np.outer(A,B)
print(outProduct)
