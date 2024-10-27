#The linalg.det tool computes the determinant of an array.
import numpy
n = int(input())
def convert_string(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s
all_arr_list = []
for _ in range(n):
    arr_list = [convert_string(x) for x in input().split()]
    all_arr_list.append(arr_list)
determinant = numpy.linalg.det(all_arr_list)
print(round(determinant,2))