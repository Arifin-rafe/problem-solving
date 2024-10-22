if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command, *items = input().split()
        if command == "insert":
            list.insert(int(items[0]),int(items[1]))
        elif command == "remove":
            list.remove(int(items[0]))
        elif command == "append":
            list.append(int(items[0]))
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        elif command == "print":
            print(list)

