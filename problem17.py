# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.


n = input("Total country name : ")
c_set = set()
tuple_set = tuple(c_set)
for _ in range(int(n)):
    c_name = input("Country name : ")
    c_set.add(c_name)
print(c_set)   
for c in c_set:
    print(c)
print(len(c_set))