total_element = int(input())
a = input().split()
total_command = int(input())
a_set = {int(x) for x in a}
for _ in range(total_command):
    command = input().split()
    elements = input().split()
    elements_set = {int(x) for x in elements}
    if command[0] == "intersection_update":
        a_set.intersection_update(elements_set)
        print(a_set)
    elif command[0] == "update":
        a_set.update(elements_set)
        print(a_set)
    elif command[0] == "symmetric_difference_update":
        a_set.symmetric_difference_update(elements_set)
        print(a_set)
    elif command[0] == "difference_update":
        a_set.difference_update(elements_set)
        print(a_set)
dd = sum(a_set)
print(dd)