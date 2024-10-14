#capitalize

n = input("Enter name : ").split()

name_list =[x for x in n]
upper_list = []
index = 0
for name in name_list:
    if name[0] != name[0].isupper():
        name = name[0].upper() + name[1:]
        upper_list.append(name)
# print(name_list)
new_join= " ".join(x for x in upper_list)
print(new_join)