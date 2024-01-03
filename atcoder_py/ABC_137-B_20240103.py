num_range, coord = map(int, input().split())
ans = []
for i in range(max(-1000000, coord - num_range + 1), min(1000001, coord + num_range)):
    ans.append(str(i))

print(' '.join(ans))