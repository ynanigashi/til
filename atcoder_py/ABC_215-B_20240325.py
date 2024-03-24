n = int(input())
answer = 0
while 2**answer <= n:
    answer += 1

print(answer-1)