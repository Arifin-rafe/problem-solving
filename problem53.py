import numpy

n = input().split()
a = [float(x) for x in n]
print(a)
my_array = numpy.array(a)
f = numpy.floor(my_array)
c = numpy.ceil(my_array)
r = numpy.rint(my_array)
print(f)
print(c)
print(r)
