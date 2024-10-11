width, height = map(int, input().split())
print("4:3" if width / height == 4 / 3 else "16:9")