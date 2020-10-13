import numpy as np

N = int(input())
array = np.array([input().strip().split() for i in range(N)],float)
determinant_of_an_array = np.linalg.det(array)
print(round(determinant_of_an_array , 2))
