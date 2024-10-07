#set easy
e = int(input("Total number students fo english news: "))
e_set = set(map(int, input().split()))
f = int(input("Total number students fo french news: "))
f_set = set(map(int, input().split()))

union = e_set & f_set

print(len(union))