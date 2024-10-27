import numpy

def arrays(arr):
    mm = [x for x in arr]
    mm.reverse()
    my_arr = numpy.array(mm,float)
    return my_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)