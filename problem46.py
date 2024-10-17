from itertools import combinations_with_replacement

a = input().split()
a_list = [x for x in a[0]]
co_re= sorted(list(combinations_with_replacement(a_list,int(a[1]))))
new_list = []
for i in co_re:   
    mm=''.join(sorted(i))
    new_list.append(mm)
lala=sorted(new_list)
for i in lala:
    print(i)