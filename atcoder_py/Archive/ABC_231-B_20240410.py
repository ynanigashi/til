num_of_boat = int(input())
canditates = {}
for _ in range(num_of_boat):
    boat = input()
    if boat in canditates:
        canditates[boat] += 1
    else:
        canditates[boat] = 1

print(max(canditates, key=canditates.get))