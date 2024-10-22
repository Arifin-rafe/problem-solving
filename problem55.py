import numpy
# learn inner and outer
a = input().split()
b = input().split()
a_list =[int(x) for x in a]
b_list =[int(x) for x in b]

a_arr = numpy.array(a_list)
b_arr = numpy.array(b_list)
print(numpy.inner(a_arr,b_arr))
print(numpy.outer(a_arr,b_arr))