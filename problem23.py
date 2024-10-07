
if __name__ == '__main__':
    n = int(input("Total number : "))
    arr = map(int, input().split())
    a= set(x for x in arr)
    b= [x for x in a]
    c= sorted(b)
    if len(c) >= 2:
        print(c[-2])
    else:
        print(c)