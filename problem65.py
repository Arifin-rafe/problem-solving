from collections import namedtuple
n = int(input())

for _ in range(n):
    pri,mil,col,clss = input().split()
    Car = namedtuple('Car','Price Mileage Colour Class')
    xyz = Car(Price = int(pri), Mileage = int(mil), Colour = col, Class = clss)

print (xyz)
print (xyz.Class)