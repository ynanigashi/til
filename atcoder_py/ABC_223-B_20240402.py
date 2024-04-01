strings = input()
shifted_strings = set()
for i in range(len(strings)):
    shifted_strings.add(strings[i:] + strings[:i])

shifted_strings = sorted(list(shifted_strings))
print(shifted_strings[0])
print(shifted_strings[-1])