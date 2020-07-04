if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=(sorted(set(arr)))
    print(l[-2])