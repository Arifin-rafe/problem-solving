import numpy

n,m = input().split()

a = []
b = []

for _ in range(int(n)):
    x = [int(i) for i in input().split()]
    a.append(x)
for _ in range(int(n)):
    x = [int(i) for i in input().split()]
    b.append(x)
    
a_arr = numpy.array(a)
b_arr = numpy.array(b)

print(numpy.add(a_arr,b_arr,))
print(numpy.subtract(a_arr,b_arr))
print(numpy.multiply(a_arr,b_arr))
print(numpy.floor_divide(a_arr,b_arr))
print(numpy.mod(a_arr,b_arr))
print(numpy.power(a_arr,b_arr))