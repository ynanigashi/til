s = input()
answer = ''
for c in s[::-1]:
    if c == '6':
        answer += '9'
    elif c == '9':
        answer += '6'
    else:
        answer += c

print(answer)