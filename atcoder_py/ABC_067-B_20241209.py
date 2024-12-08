num_of_length, num_of_cut = map(int, input().split())
lengths = list(map(int, input().split()))
lengths.sort(reverse=True)
print(sum(lengths[:num_of_cut]))