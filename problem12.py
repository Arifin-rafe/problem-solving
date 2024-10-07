def mutate_string(string, position, character):
    my_s= list(string)
    my_s[position] = character
    new_s =''.join(my_s)
    return new_s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)