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

# The Cartesian product of two sets A and B is the set of all possible pairs where the first element comes from A and the second from B

# Use Cases:
# Generating all combinations: Useful when you need all possible combinations of two or more lists (e.g., generating all coordinates in a grid).

# Nested Loops Simplification: Instead of writing nested loops to get combinations of multiple iterables, itertools.product() does this efficiently.