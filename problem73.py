import re
p = r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[a-zA-Z0-9]{10}$'
for _ in range(int(input())):
    s = input()
    print("Valid" if re.match(p, s) and len(s) == len(set(s)) else "Invalid")