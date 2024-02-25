max_num = int(input())
include_7_count = 0
for i in range(1, max_num+1):
    if '7' in str(i) or '7' in oct(i):
        include_7_count += 1

print(max_num - include_7_count)