len_of_sequence = int(input())
sequence = list(map(int, input().split()))
min_num = sequence[0]
cnt = 0
for i in sequence:
    if i <= min_num:
        cnt += 1
        min_num = i
print(cnt)