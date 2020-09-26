import numpy as np

n,m = map(int,input().split()) #user input for rows and columns

Numpy_array = np.array([input().strip().split() for i in range(n)],int)#Input elements of array under a given range n

sum_along_axis=np.sum(Numpy_array,axis=0) #sum of a numpy array, axis=0 means add elements vertically
#print(sum_along_axis)

productOf_sum_along_axis = np.prod(sum_along_axis) #product of sum_result
print(productOf_sum_along_axis)
