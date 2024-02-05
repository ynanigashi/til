num_of_lookouts, num_of_road = map(int, input().split())
hights = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(num_of_road)]
ans = 0
road_of_lookouts = {i: [] for i in range(1, num_of_lookouts+1)}
for road in roads:
    road_of_lookouts[road[0]].append(road[1])
    road_of_lookouts[road[1]].append(road[0])

for i in range(1, num_of_lookouts+1):
    if not road_of_lookouts[i]:
        ans += 1
    else:
        max_hight = max([hights[j-1] for j in road_of_lookouts[i]])
        if hights[i-1] > max_hight:
            ans += 1

print(ans)