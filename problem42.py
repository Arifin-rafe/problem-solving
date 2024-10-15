from itertools import product
a = input().split()
b = input().split()
a_list = [int(x) for x in a]
b_list = [int(x) for x in b]
itr = list(product(a_list,b_list))
mt= ''
for i in itr:
    mt+=str(i) + " "
print(mt)
