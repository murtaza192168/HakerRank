A = set(map(int,input().split()))

n = int(input())
N = set(map(int,input().split()))

print(N.issuperset(A))
