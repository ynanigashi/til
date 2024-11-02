balls, colors = map(int, input().split())
print(colors * (colors - 1) ** (balls - 1))