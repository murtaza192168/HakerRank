 

K,array = int(input()) , list(map(int,input().split()))

set_1 = set(array)
# mult=(sum(set_1)*K)-sum(array)
# divsn=mult//(K-1)
# Captain_room_number=mult-divsn
# print(Captain_room_number)

manipulate=(((sum(set_1)*K)-(sum(array))))    
room_num = manipulate//(K-1)
print(room_num)
