# ABCDCDC sample input
# CDC
#not solved
def count_substring(string, sub_string):
    new_list = []
    for i in range(0, len(string)):
        for x in range(0,len(sub_string)): 
            if (string[i]) == sub_string[x]:
                new_list.append(sub_string[x])
    match_strings = ""
    for i in new_list:
        match_strings+=i
    count_of_sub_string = match_strings.count(sub_string)
    print(new_list)       
    return count_of_sub_string

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)