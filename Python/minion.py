def minion_game(string):
    S=0
    K=0
    vowels = ['A','E','I','O','U']
    for i in range(len(string)):
        if string[i] in vowels:
            K = K + len(string) - i
        else:
             S = S + len(string) - i
             
    if S > K:
        print("Stuart" + " " + "%d" %S)    
    elif S < K:
        print("Kevin" + " " + "%d" %K)  
    else:
        print("Draw")           
                
     
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
