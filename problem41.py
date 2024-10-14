#polar coordinates

import cmath
n = complex(input())
c_match = cmath.polar(n)
for i in c_match:
    print (i)
    
#In Python, the cmath.polar() function is used to convert a complex number into its polar coordinate representation. Polar coordinates represent a complex number in terms of its magnitude (or modulus, the distance from the origin) and phase angle (or argument, the angle made with the positive real axis).

#cmath.polar() is useful when working with complex numbers and when you need to switch from Cartesian (rectangular) form to polar form in mathematical or engineering applications.