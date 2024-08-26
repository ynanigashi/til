len_sequence, max_num = map(int, input().split())
sequence = list(map(int, input().split()))
flags = [False] * max_num
for i in range(len_sequence):
    if sequence[i] <= max_num:
        flags[sequence[i] - 1] = True

for i in range(len_sequence):
    for j in range(i + 1, len_sequence):
        temp_sum = sequence[i] + sequence[j]
        if temp_sum <= max_num:
            flags[temp_sum - 1] = True

for i in range(len_sequence):
    for j in range(i + 1, len_sequence):
        for k in range(j + 1, len_sequence):
            temp_sum = sequence[i] + sequence[j] + sequence[k]
            if temp_sum <= max_num:
                flags[temp_sum - 1] = True

print(flags.count(True))