n,m = map(int,input().split())           #n=7,m=n*3

for i in range(1,n,2):                   #(start range,end range,interval) 1->3->5->7
    print((i*".|.").center(m,'-'))       #m=21=width i.e.--> str.center(width,filling_character)
    
print("WELCOME".center(m,"-"))            #As we want to print oly once

for i in range(n-2,-1,-2):
    print((i*".|.").center(m,"-"))
