import numpy as np

N,M,P = map(int,input().split())

my_array = np.array([input().strip().split() for i in range(N) ],int)
my_array1 =np.array([input().strip().split() for i in range(M) ],int) 
ConcatenatedArray=np.concatenate((my_array,my_array1),axis=0)
print(ConcatenatedArray)
