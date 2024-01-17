num_of_bricks = int(input())
bricks = list(map(int, input().split()))
index = 1
for brick in bricks:
    if brick == index:
        index += 1
print(len(bricks) - (index - 1) if index != 1 else -1)