from collections import defaultdict

n , m =map(int , input().split(' '))

N = list()                       
for i in range(n):
    N.append(input())
M=list()    
for i in range(m):
    M.append(input())

#calculating Output    

d = defaultdict(list) # Function to return a default  values for keys that is not present
                                      
                                    

for i in range(n):
    d[N[i]].append(i+1)        # now put the input N elements in d i.e defaultDictionary(append it)

#LOGIC
for i in M:                    #for each item in M i.e input elements of m, 
                               #check if that same item is present in defaultdict...
    if i in d:
        print(*d[i])
    else:
        print(-1)        

