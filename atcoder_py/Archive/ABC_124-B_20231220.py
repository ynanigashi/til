_ = input()
heights = list(map(int, input().split()))
max_height = heights[0]
cnt = 0
for height in heights:
    if height >= max_height:
        max_height = height
        cnt += 1

print(cnt)