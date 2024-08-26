max_height = int(input())
height = 1
day = 0
while height <= max_height:
    day += 1
    height += 2**day

print(day+1)