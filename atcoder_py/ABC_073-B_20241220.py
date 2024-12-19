num_of_inputs = int(input())
ans = 0
for _ in range(num_of_inputs):
    l, r = map(int, input().split())
    ans += r - l + 1

print(ans)