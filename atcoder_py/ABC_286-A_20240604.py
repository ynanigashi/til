_, p, q, r, s = map(int, input().split())
seqs = list(map(int, input().split()))
seqs[p-1:q], seqs[r-1:s] = seqs[r-1:s], seqs[p-1:q]
print(*seqs)