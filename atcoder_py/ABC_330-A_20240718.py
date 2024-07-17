len_of_seqs, min_num = map(int, input().split())
seqs = list(map(int, input().split()))
seqs = [i for i in seqs if i >= min_num]
print(len(seqs))