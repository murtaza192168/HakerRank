def average(array):
    set1 = set(array)
    avg = sum(set1) / len(set1)
    return avg
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
