s = input()
i = 0
answer = ''
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    answer += '{}{}'.format(s[i], j-i)
    i = j
print(answer)
