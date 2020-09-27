import numpy as np

n, m=map(int,input().split())
numpy_arr=np.array([input().strip().split() for i in range(n)],int)

numpy_mean=np.mean(numpy_arr,axis=1)
print(numpy_mean)
numpy_var=np.var(numpy_arr,axis=0)
print(numpy_var)
numpy_std=np.std(numpy_arr,axis=None)
print("{0:.11f}".format(numpy_std))



