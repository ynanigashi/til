num_of_input = int(input())
ans = 0
for i in range(num_of_input):
    l, r = map(int, input().split())
    ans += r - l + 1
print(ans)