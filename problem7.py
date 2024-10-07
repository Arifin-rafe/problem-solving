# Given an integer, n, and n space-separated integers as input, create a tuple,t , of those  integers. Then compute and print the result of . 

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Read the integer n
n = int(input())

# Read the space-separated integers and create a tuple
numbers = map(int, input().split())
t = tuple(numbers)

# Compute and print the hash of the tuple
print(hash(t))

