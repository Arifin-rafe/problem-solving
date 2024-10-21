import numpy
a = [float(x) for x in input().split()]
my_array = numpy.array(a)
print (numpy.floor(my_array))
print (numpy.ceil(my_array))
print (numpy.rint(my_array))