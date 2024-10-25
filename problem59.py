import numpy

def convert_string(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s
final = numpy.polyval(list(convert_string(x) for x in input().split()), int(input()))
print (float(final))