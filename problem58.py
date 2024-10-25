#learn numpy dot and cross

import numpy

n = input()

my_arr_a = []
my_arr_b = []

for _ in range(int(n)):
    total_arr = input().split()
    arr = [int(x) for x in total_arr]
    my_arr_a.append(arr)
for _ in range(int(n)):
    total_arr = input().split()
    arr = [int(x) for x in total_arr]
    my_arr_b.append(arr)
    
final_arr = numpy.array(my_arr_a)
final_arr2 = numpy.array(my_arr_b)

print(numpy.dot(final_arr,final_arr2))