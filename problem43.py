from itertools import permutations

a = input().split()
a_list = [x for x in a[0]]
perm = sorted(list(permutations(a_list,int(a[1]))))

for i in perm:
    mm=''.join(i)
    print(mm)
