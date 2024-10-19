n = input().split()
gg = []
def convert_string(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s
for _ in range(int(n[1])):
    mm = input().split()
    gg.append(tuple(convert_string(x) for x in mm))
zipped = tuple(zip(*gg))
print(zipped)

for i in range(len(zipped)):
    mama = sum(zipped[i])
    print(round(mama/len(zipped[i]),2))




