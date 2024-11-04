min_num, max_num, div_num = map(int,input().split())
max_div = max_num // div_num
min_div = (min_num - 1) // div_num if min_num - 1 > 0 else 0
print(max_div - min_div)