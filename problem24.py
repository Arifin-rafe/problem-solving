if __name__ == '__main__':
    records = []
    for _ in range(int(input("Total student record : "))):
        name = input("Student name : ")
        score = float(input("Student score : "))
        records.append([name,score])
score_list = set()
for x in records:
    score_list.add(x[1])
my_score_list = set(score_list)
my_sort_score = sorted(my_score_list)

print(my_sort_score)

name_list = []
for x in records:
    if x[1] == my_sort_score[1]:
        name_list.append(x[0])
my_sort_name_list = sorted(name_list)

for name in my_sort_name_list:
    print(name)