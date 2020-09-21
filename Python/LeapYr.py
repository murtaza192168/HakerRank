if __name__ == '__main__':
    n = int(input())

    for i in range(0,n):
        print(i*i)

##################################################3
##LeapYear##

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4) == 0:
        if (year%100) == 0:
            if (year%400) == 0:
                return True
            else:
                return False
                 
        else:
            return True
            
        
    else:
         return False
         


  

    
    return leap

year = int(input())
print(is_leap(year))
