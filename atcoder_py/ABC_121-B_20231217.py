num_of_source_codes, num_of_features, c = map(int, input().split())
multipliers = list(map(int, input().split()))
source_codes = [list(map(int, input().split())) for _ in range(num_of_source_codes)]
cnt = 0
for source_code in source_codes:
    if sum([multipliers[i] * source_code[i] for i in range(num_of_features)]) + c > 0:
        cnt += 1
print(cnt)