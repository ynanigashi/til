num_of_strs, num_of_targets = map(int, input().split())
strs = [input()[3:] for _ in range(num_of_strs)]
targets = {input() for _ in range(num_of_targets)}
cnt = 0
for s in strs:
    if s in targets:
        cnt += 1
print(cnt)
