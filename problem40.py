#capitalize
#not solved
n = input("Enter name : ").strip().split()

name_list =""

for name in name_list:
    if name==name.isupper():
        name = name[0].upper() + name[1:]
        upper_list.append(name)
# print(name_list)
new_join= " ".join(x for x in upper_list)
print(new_join)