#learn shape
import numpy
n= input().split()
change_arr = numpy.array([int(x) for x in n])
change_arr.shape = (3,3)
print(change_arr)