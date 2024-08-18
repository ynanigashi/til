num_of_seq, k, x = map(int, input().split())
seq = list(map(int, input().split()))
seq.insert(k, x)
print(*seq)