def custom_round(value):
    if value - int(value) == 0.5:
        return int(value) + 1
    else:
        return round(value)

num, num_of_round = map(int, input().split())
for i in range(1, num_of_round+1):
    round_num = 10**i
    num = custom_round(num / round_num)*round_num

print(num)