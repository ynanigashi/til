import re
s = input()

result = re.fullmatch(r'^A[a-z]+C[a-z]+$', s)

answer = 'WA' if result == None else 'AC'

print(answer)