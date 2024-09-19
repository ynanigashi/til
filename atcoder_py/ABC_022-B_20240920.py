num_of_inputs = int(input())
already_seen = set()
ans = 0
for i in range(num_of_inputs):
    num = int(input())
    if num in already_seen:
        if i > num: ans += 1
    else:
        already_seen.add(num)

print(ans)