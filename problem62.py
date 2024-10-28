import numpy

n,m = input().split()

new_arr=[]
for _ in range(int(n)):
    mm = [int(x) for x in input().split()]
    new_arr.append(mm)
y_arr = numpy.array(new_arr)
sums = numpy.sum(y_arr,axis=0)
print(numpy.prod(sums,axis=0))