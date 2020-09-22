nOfStuEngNew = int(input()) 
StuRollNoE = set(map(int,input().split()))

nOfStuFrnchNew = int(input())
StuRollNoF = set(map(int,input().split()))

intersectionn=StuRollNoE.intersection(StuRollNoF)
result=len(intersectionn)
print(result)
