def print_formatted(n):
    num=len(str(bin(n)).replace('0b',''))

    for i in range(1,n+1):

        binary = bin(int(i)).replace('0b','').rjust(num,' ')
        octal = oct(int(i)).replace('0','').rjust(num,' ')
        hexadec = hex(int(i)).replace('0x','').upper().rjust(num,' ')
        j = str(i).rjust(num,' ')
        print (j,octal,hexadec,binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
