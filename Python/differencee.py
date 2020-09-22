nOfStuEngNew = int(input()) 
StuRollNoE = set(map(int,input().split()))

nOfStuFrnchNew = int(input())
StuRollNoF = set(map(int,input().split()))

differences=StuRollNoE.difference(StuRollNoF)
result=len(differences)
print(result)
