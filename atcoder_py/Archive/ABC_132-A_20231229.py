target_str = input()
print('Yes' if len(set(target_str)) == 2 and target_str.count(target_str[0]) == 2 else 'No')