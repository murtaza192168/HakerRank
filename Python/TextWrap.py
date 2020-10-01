import textwrap

def wrap(string, max_width):

    wrap_up=textwrap.fill(string,max_width)

    
    return wrap_up

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
