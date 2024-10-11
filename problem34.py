a = input("Set A element : ").split()
a_set = set(int(x) for x in a)
n = input("length : ")
other_set_list = []
for _ in range(int(n)):   
    mm = input("Other set elements : ").split()
    other_set = set(int(x) for x in mm)
    other_set_list.append(other_set)
    subset_validation_string = ""
    for i in other_set_list:
        if not a_set > i:
            subset_validation_string += "0"
        else: 
            subset_validation_string += "1"
    # print(pp)
if "0" in subset_validation_string:
    print(False)
else:
    print(True)       
    
    
