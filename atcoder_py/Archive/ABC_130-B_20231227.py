num_of_bounds, max_length = map(int, input().split())
lengths = list(map(int, input().split()))
cnt = 1
former_sum = 0
for length in lengths:
    former_sum += length
    if former_sum <= max_length:
        cnt += 1
    else:
        break
print(cnt)