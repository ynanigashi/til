num_of_height = int(input())
heights = list(map(int, input().split()))
answer = 0
for height in heights:
    if answer < height:
        answer = height
    else:
        break
print(answer)