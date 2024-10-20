#learn about eval.. it makes a string to a python expression
n = input().split()
p = input()

x=int(n[0])
k=n[1]
z=eval(p)
if z == int(k):
    print(True)
else:
    print(False)