from itertools import permutations

#unsolved
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input("total : "))
    
    cre_list1 = permutations([i for i in range(x+1) if i<=x],3)
    cre_list2 = permutations([i for i in range(y+1) if i<=y],3)
    cre_list3 = permutations([i for i in range(z+1) if i<=z],3)
    my_list = list(cre_list1),list(cre_list2),list(cre_list3)
    # my_list.append(cre_list2)
    # my_list.append(cre_list3)
    print(my_list)