import numpy as np

numpyArray_elements = np.set_printoptions(sign=' ')
numpyArray_elements = np.array(input().split() , float)
 
convrt_floor=np.floor(numpyArray_elements)
print(convrt_floor)

convrt_ceil=np.ceil(numpyArray_elements)
print(convrt_ceil)

convrt_rint=np.rint(numpyArray_elements)
print(convrt_rint)
