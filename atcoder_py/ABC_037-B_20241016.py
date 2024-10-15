len_of_seq, num_of_operation = map(int, input().split())
seq = [0] * len_of_seq
for _ in range(num_of_operation):
    l, r, v = map(int, input().split())
    for i in range(l - 1, r):
        seq[i] = v

for i in seq:
    print(i)