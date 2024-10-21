import numpy

j = input().split()
n = int(j[0])
m = int(j[1])
p = int(j[2])
lala =[]
pala =[]
for _ in range(n):
    mm = [int(x) for x in input().split()]
    lala.append(mm)
for _ in range(m):
    mm = [int(x) for x in input().split()]
    pala.append(mm)

arr = numpy.array(lala)
arr1 = numpy.array(pala)
print(numpy.concatenate((arr,arr1),axis = 0))