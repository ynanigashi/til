low, high = map(int, input().split())
num_of_weeks = int(input())
for _ in range(num_of_weeks):
    num = int(input())
    if num < low:
        print(low - num)
    elif num > high:
        print(-1)
    else:
        print(0)