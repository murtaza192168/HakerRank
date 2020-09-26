import numpy as np
n , m = map(int ,input().split()) #user input rows and columns

Numpy_array=np.array([input().strip().split() for i in range(n)],int)
minimumOfArray = np.min(Numpy_array , axis=1) #axis=1 means comparsion of numpy array horizontally 

maxEle_Of_minArray = np.max(minimumOfArray)  #maximum element found out from minimum array elements
print(maxEle_Of_minArray)


