string = input()
substring = input()
min_diff = len(substring)
for i in range(len(string) - len(substring) + 1):
    diff = 0
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            diff += 1
    min_diff = min(min_diff, diff)

print(min_diff)