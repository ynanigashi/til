num_str = input()
min_diff = 1000
for i in range(len(num_str) - 2):
    min_diff = min(min_diff, abs(int(num_str[i:i+3]) - 753))
print(min_diff)