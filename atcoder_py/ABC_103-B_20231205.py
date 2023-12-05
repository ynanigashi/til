string = input()
target_str = input()
for i in range(len(string)):
    if target_str == string[i:] + string[:i]:
        print('Yes')
        break
else:
    print('No')