N = int(input())
int_list = [0 for _ in range(N+1)]
ans = 0
for i in range(1, N+1):
    for j in range(i, N+1, i):
        int_list[j] += 1
for i, cnt in enumerate(int_list): ans += i*cnt
print(ans)