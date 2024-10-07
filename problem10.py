def split_and_join(line):
    # write your code here
    my_line = line.split(" ")
    my_line = "-".join(my_line)
    return my_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)