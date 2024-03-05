# 3.7以降順番が保持される
results = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
num_of_results = int(input())
for _ in range(num_of_results):
    results[input()] += 1

for key, value in results.items():
    print(f'{key} x {value}')