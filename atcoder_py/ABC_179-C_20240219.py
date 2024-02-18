n = int(input())
answer = 0
for i in range(1, n):
    answer += (n - 1) // i

print(answer)