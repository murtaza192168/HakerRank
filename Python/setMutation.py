a = int(input())
A=set(map(int,input().split()))

N=int(input())
for i in range(N):
    op , length = (input().split())
    B = set(map(int,input().split()))

    if op == "intersection_update":
        A.intersection_update(B)
    elif op=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif op=="difference_update":
        A.difference_update(B)
    elif op=="update":
         A.update(B)

print(sum(A))         


    
