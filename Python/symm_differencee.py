
nOfStuEngNew = int(input()) 
StuRollNoE = set(map(int,input().split()))

nOfStuFrnchNew = int(input())
StuRollNoF = set(map(int,input().split()))

symm_differences=StuRollNoE.symmetric_difference(StuRollNoF)
result=len(symm_differences)
print(result)
