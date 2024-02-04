num_of_times, addend = [int(input()) for _ in range(2)]
ans = 1
for _ in range(num_of_times):
     ans += addend if ans >= addend else ans
print(ans)