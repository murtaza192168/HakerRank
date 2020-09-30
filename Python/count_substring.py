def count_substring(string, sub_string):

    count = 0
    i = string.find(sub_string)          #find() is used to find the substring from the string

    while i != -1:                     #will return true, i.e. there should be atleast one substring. as indexing starts from 0, I hav put -1 as empty 
        count += 1
        i = string.find(sub_string , i+1)
            

  
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)       #calling function and display in the main
    print(count)
