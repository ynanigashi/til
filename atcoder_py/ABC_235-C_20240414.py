len_of_sequence, num_of_queries = map(int, input().split())
sequence = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(num_of_queries)]
first_appearance = {}
for i, num in enumerate(sequence):
    # ajust index
    i += 1
    if num not in first_appearance:
        first_appearance[num] = [i]
    else:
        first_appearance[num].append(i)

for query in queries:
    num, k = query
    answer = -1
    if num in first_appearance and len(first_appearance[num]) >= k:
        answer = first_appearance[num][k-1]
    print(answer)

    