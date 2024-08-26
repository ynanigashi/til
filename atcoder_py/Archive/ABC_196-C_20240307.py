#TLE
'''
n = int(input())
answer = 0
i = 1
while i <= n:
    if len(str(i)) % 2 == 1:
        i *= 10
        continue

    if str(i) == str(i)[::-1]:
        answer += 1
    i += 1

print(answer)

'''

N = int(input())
for i in range(1, 1000001):
    if int(str(i) * 2) > N:
        print(i - 1)
        exit()