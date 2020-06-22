x_list = list(map(int, input().split()))
for i, num in enumerate(x_list):
    if num == 0:
        print(i+1)
        break 