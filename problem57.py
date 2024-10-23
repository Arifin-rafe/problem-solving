#learn numpy mean var std
import numpy
n = input().split()
append_arr = []
for _ in range(int(n[0])):
    total_arr = input().split()
    arr = [int(x) for x in total_arr]
    append_arr.append(arr)
my_array = numpy.array(append_arr)
mean_arr = numpy.mean(my_array, axis = 1)
var_arr = numpy.var(my_array, axis = 0)
std_arr = numpy.std(my_array, axis = None)
print (mean_arr)       
print (var_arr)       
print (numpy.round(std_arr,11))