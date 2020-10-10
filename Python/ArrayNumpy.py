import numpy

def arrays(arr):
   
    npArray=numpy.array(arr,float)
    reverseArray = npArray[::-1]
    return (reverseArray)
  

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
