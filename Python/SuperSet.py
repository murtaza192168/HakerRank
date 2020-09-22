A = set(map(int,input().split()))

n = int(input())
status = True #assuring that A is subset of n sets
for i in range(n):
    N = set(map(int,input().split()))
    current = A.issuperset(N) 
    status=status and current
print(status)    
