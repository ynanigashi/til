height, width = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(height)]
min_blocks = min([min(row) for row in grid])
print(sum([sum(row) for row in grid]) - min_blocks * height * width)