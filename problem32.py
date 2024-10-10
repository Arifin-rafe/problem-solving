if __name__ == '__main__':
    s = input()
print(any(alphanumeric.isalnum() for alphanumeric in s))
print(any(alphabet.isalpha() for alphabet in s))
print(any(digit.isdigit() for digit in s))
print(any(lower.islower() for lower in s))
print(any(upper.isupper() for upper in s))
