#Check Subset

test_cases = int(input("Total test cases : "))

for _ in range(test_cases):
    total_a_elem = int(input("Total elements of set A : "))
    a_elem = input("elements of set A : ").split()
    a_set ={int(x) for x in a_elem}
    total_b_elem = int(input("Total elements of set b : "))
    b_elem = input("elements of set B : ").split()
    b_set ={int(x) for x in b_elem}
    if a_set <= b_set:
        print(True)
    else:
        print(False)
     