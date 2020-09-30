if __name__ == '__main__':
    s = input()
    l=list(s)
    p=q=r=t=u=False#initially

    for i in l:
        if i.isalnum():
            p=True
        if i.isalpha():
            q=True
        if i.isdigit():
            r=True
        if i.islower():
            t=True
        if i.isupper():
            u=True
            
    print(p)
    print(q)
    print(r)
    print(t)
    print(u)    

