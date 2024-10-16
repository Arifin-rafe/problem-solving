from itertools import permutations

a = input().split()
a_list = [x for x in a[0]]
perm = sorted(list(permutations(a_list,int(a[1]))))

for i in perm:
    mm=''.join(i)
    print(mm)

# Important Notes:
# Permutations are ordered combinations, meaning the order of elements matters.
# The number of permutations of a set with n elements is n! (factorial of n). For example, a list with 3 elements has 3! = 6 permutations.

#Use Cases:Rearranging elements to check all possible outcomes (useful in puzzles, games, optimization problems).Generating all possible sequences for testing purposes or exploring data.