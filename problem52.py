#learn about deque. it actually add and delete from the both side of a list
from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    id_s = input().split()
    
    if id_s[0] == 'append':
        d.append(id_s[1])
        print(d)
    elif id_s[0] == "appendleft":
        d.appendleft(id_s[1])
        print(d)
    elif id_s[0] == "pop":
        d.pop()
        print(d)
    elif id_s[0] =="popleft":
        d.popleft()
        print(d)

x = " ".join(x for x in d)
print(x)