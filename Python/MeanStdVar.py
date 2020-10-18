import numpy as np
n , m = map(int,input().split())
my_arr = np.set_printoptions(legacy = '1.13')
my_arr=np.array([input().strip().split() for i in range(n)],int)

mean = np.mean(my_arr,axis=1)
print(mean)
variance = np.var(my_arr,axis=0)
print(variance)
standard_deviation = np.std(my_arr)
print(standard_deviation)
