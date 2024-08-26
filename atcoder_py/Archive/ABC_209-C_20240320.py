N = int(input())
C = list(map(int, input().split()))
C.sort()
answer=1
for i in range(N):
    answer = answer * max(0, C[i] - i) % 1000000007
print(answer)
