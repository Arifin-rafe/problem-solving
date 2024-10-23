#learn numpy min max 
import numpy
n = input().split()
ll = []
for _ in range(int(n[0])):
    total_arr = input().split()
    arr = [int(x) for x in total_arr]
    ll.append(arr)
my_array = numpy.array(ll)
a = numpy.min(my_array, axis = 1)
print (max(a))        
