#capitalize
#not solved
n = input("Enter name : ").strip().split()

name_list =""

for name in name_list:
    if name==name.isupper():
        name = name[0].upper() + name[1:]
        name_list.append(name)
# print(name_list)
new_join= " ".join(x for x in name_list)
print(new_join)