N = int(input())
int_list = [0 for _ in range(N+1)]
int_list[1] = 1
ans = 1
for i in range(2, N+1):
    f = int_list[i//2]+1 if i%2 == 0 else 2
    int_list[i] = f
    ans += f*i
print(ans)