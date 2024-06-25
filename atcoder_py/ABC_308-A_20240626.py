len_of_seq = 8
seq = list(map(int, input().split()))
if seq[0] < 100 or seq[0] % 5 != 0 or seq[-1] > 675:
    print('No')
    exit()

for i in range(len_of_seq - 1):
    if seq[i] >= seq[(i+1)] or seq[i]%25 != 0:
        print('No')
        break
else:
    print('Yes')
    