#itertools.combinations
from itertools import combinations
n = input().split()
sort_list=[]
for i in range(1,int(n[1])+1):
    n_combinations = sorted(list(combinations(n[0],i)))
    for i in n_combinations:
        mm = sorted(i)
        join_tuple = ''.join(mm)
        sort_list.append(join_tuple)
        #tow ways to sort here first sort alphabetically then using length
# def sort_key(item):
#     return (len(item), item)
# sorted_list = sorted(sort_list, key=sort_key)
sorted_list = sorted(sort_list, key=lambda x: (len(x), x))
        
for i in sorted_list:
    print(i)
