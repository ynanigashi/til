len_of_str = int(input())
str = input()
print('Yes' if str[len_of_str//2:] == str[:len_of_str//2] else 'No')