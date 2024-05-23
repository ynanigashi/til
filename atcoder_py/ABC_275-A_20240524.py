num_of_bridges = int(input())
heights_of_bridges = list(map(int, input().split()))
bridges = []
for i in range(num_of_bridges):
    bridges.append((heights_of_bridges[i], i))

bridges.sort(reverse=True)

print(bridges[0][1] + 1)