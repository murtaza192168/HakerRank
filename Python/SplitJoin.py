def split_and_join(line):
    splt=line.split(' ')
    jn = '-'.join(splt)
    return jn    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
