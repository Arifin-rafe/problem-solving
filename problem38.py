n = int(input("Total num : "))
t_f_list = []
# num = []
for _ in range(n):
    m = input()
    # print(type(m))
    # num.append(float(m))
    # for i in num:    
    if type(m) == float:
        t_f_list.append(True)
    else:
        t_f_list.append(False)
print(t_f_list)
# print(num)
for i in t_f_list:
    print(i)