height, width = map(int, input().split())
i, j = map(int, input().split())
adjacent = 0
if 1 < i <= height:
    adjacent += 1
if i < height:
    adjacent += 1

if 1 < j <= width:
    adjacent += 1

if j < width:
    adjacent += 1

print(adjacent)
