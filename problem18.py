#set easy

n = int(input("Total number in string : "))
s = set(map(int, input().split()))
c = int(input("TOTAL COMMAND : "))
print(s)
for _ in range(c):
    cmd = input("Command and number : ").split()
    # print(cmd[1])
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] =="remove":
        s.remove(int(cmd[1]))
    elif cmd[0] =="discard":
        s.discard(int(cmd[1]))
print(s)   
total = sum(s)
print(total)