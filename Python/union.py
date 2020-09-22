nOfStuEngNew = int(input())                      
StuRollNoE = set(map(int,input().split()))  #input of sets based on range provided

nOfStuFrnchNew = int(input())
StuRollNoF = set(map(int,input().split()))

union=StuRollNoE.union(StuRollNoF)      #logic
result=len(union)
print(result)
