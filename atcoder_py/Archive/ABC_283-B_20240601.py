len_of_seqs = int(input())
seqs  = list(map(int, input().split()))
num_of_queries = int(input())
queries = [list(map(int, input().split())) for _ in range(num_of_queries)]

for query in queries:
    if query[0] == 1:
        seqs[query[1] - 1] = query[2]
    else:
        print(seqs[query[1] - 1])

