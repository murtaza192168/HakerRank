if __name__ == '__main__':
    
    n = int(input().strip())
    l = []

    for i in range(n):
        list = input().strip().split(" ")

        if list[0] == "append":
            l.append(int(list[1]))
        elif list[0] == "insert":
            l.insert(int(list[1]),int(list[2]))
        elif list[0] == "remove":
            l.remove(int(list[1]))
        elif list[0] == "sort":
            l.sort()
        elif list[0] == "pop":
            l.pop()
        elif list[0] == "reverse":
            l.reverse()
        elif list[0] == "print":
            print(l)                        
        
       
