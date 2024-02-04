def is_like_coffee(s):
    return s[2] == s[3] and s[4] == s[5]

string = input()
print('Yes' if is_like_coffee(string) else 'No')