#learn about zip

n = input().split()
append_tuple= []
def convert_string(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s
for _ in range(int(n[1])):
    total_input = input().split()
    append_tuple.append(tuple(convert_string(x) for x in total_input))
zipped = tuple(zip(*append_tuple))
print(zipped)

for i in range(len(zipped)):
    sum_tuples = sum(zipped[i])
    print(round(sum_tuples/len(zipped[i]),2))




