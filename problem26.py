n = int(input())
m = input().split()
k = int(input())
j = input().split()

a = set(int(x) for x in m if len(range(n)))
b = set(int(x) for x in j if len(range(k)))

sym_difference = a^b
sort_sym = sorted(sym_difference)
for x in sort_sym:
    print(x)
