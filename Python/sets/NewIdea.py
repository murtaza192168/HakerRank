n , m = map(int,input().split())
happiness=0

n_ele = input().split()

m_integers_setA  =set(input().split())

m_integers_setB = set(input().split())


for i in n_ele:
     if i in m_integers_setA  :
         happiness+=1
   

     if i in m_integers_setB  :
         happiness-=1
    
print(happiness)            
           
