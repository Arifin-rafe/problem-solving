#almost done

n,n2= input("Group a and b size : ").split()

a_appen = []
b_appen = []
a_list = []
b_list = []
for _ in range(int(n)):
    a= input("group A contains : ")
    a_list.append(a)
    
for _ in range(int(n2)):
    b= input("group B contains : ")
    b_list.append(b)

for idx,x in enumerate(a_list):
        if x == b_list[0]:
            a_appen.append(str(idx+1))
        elif x == b_list[1]:
            b_appen.append(str(idx+1))

a_join = " ".join(a_appen)
b_join = " ".join(b_appen)
print(a_join)
print(b_join)
