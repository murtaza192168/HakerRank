import numpy as np

N , M = map(int,input().split())

my_array = np.array([ input().strip().split() for i in range(N)],int)

Transposed_NumpyArray=np.transpose(my_array)
print(Transposed_NumpyArray)

Flattened_NumpyArray=my_array.flatten()
print(Flattened_NumpyArray)
