#learn flatten and transpose

import numpy
n = input().split()

my_arr = []
for _ in range(int(n[0])):
    pp = [int(x) for x in input().split()]
    my_arr.append(pp)
full_arr = numpy.array(my_arr)
print(numpy.transpose(full_arr))
print(full_arr.flatten())