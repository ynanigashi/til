num_of_names = int(input())
names = [input() for _ in range(num_of_names)]
print('Yes' if num_of_names != len(set(names)) else 'No')