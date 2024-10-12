import re
n = input()
yes_no = []
for _ in range(int(n)):
    number = input("Number : ")
    first_digit_find = re.search("^9",number)
    second_digit_find = re.search("^8",number)
    third_digit_find = re.search("^7",number)
    if first_digit_find or second_digit_find or third_digit_find:
        if number.isnumeric() and len(number) == 10:
            yes_no.append("YES")
        else:
            yes_no.append("NO")
    else:
        yes_no.append("NO")
        
for ans in yes_no:
    print(ans)