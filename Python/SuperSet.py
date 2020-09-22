A = set(map(int,input().split()))

n = int(input())
status = True #assuring that A is subset of n sets
for i in range(n):
    N = set(map(int,input().split()))
    current = N.issuperset(A) 
    strict_suprset_result=status and current
print(strict_suprset_result)    
