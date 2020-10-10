import numpy as np

intlist = list(map(int,input().split()))
numArrayForShape = np.array(intlist,int)
numArrayForShape.shape = (3,3)
print(numArrayForShape)
