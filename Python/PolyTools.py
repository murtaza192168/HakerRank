import numpy as np

polyArray=np.array(list(map(float,input().split())))
x = int(input())
desired_value=np.polyval(polyArray , x)
print(desired_value)

#Basically, the tool named polyval will just substitute the value..where x=value
#which would be obiviously equated to  zero'


#Example:     [1.1,2,3]>> this means:: 1.1x^2  + 2x + 3
# suppose x=0,      1.1(0)^2 + 2(0) + 3 = 0
                  #  = 3.0//output




