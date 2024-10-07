def average(array):
    # your code goes here
    total = 0
    my_set = set(array)
    for x in my_set:
        total +=x
    ave = total/len(my_set)
    return ave

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)