
def is_palindrome(num):
    return str(num) == str(num)[::-1]

n = int(input())
numbers = list(map(int, input().split())) 

all_positive = all(num > 0 for num in numbers)
any_palindromic = any(is_palindrome(num) for num in numbers)

print(all_positive and any_palindromic)
