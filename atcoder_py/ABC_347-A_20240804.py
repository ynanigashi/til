len_of_seq, k = map(int, input().split())
sequence = list(map(int, input().split()))
for i in sequence:
    if i%k == 0:
        print(int(i/k) , end = ' ')

print()