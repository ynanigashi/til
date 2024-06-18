len_of_seqs = int(input())
seqence = list(map(int, input().split()))
ans = []
for i in range(len_of_seqs-1):
    if seqence[i] < seqence[i+1]:
        pm = 1
    else:
        pm = -1

    for j in range(seqence[i], seqence[i+1], 1*pm):
        ans.append(j)

ans.append(seqence[-1])
print(*ans, sep=' ')
    