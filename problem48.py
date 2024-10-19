k = int(input())
room_list = list(map(int, input().split(' ')))
room_set = set(room_list)
for i in room_set:
    room_list.remove(i)
    if i not in room_list:
         print(i)