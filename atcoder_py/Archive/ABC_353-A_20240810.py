num_of_buildings = int(input())
hights = list(map(int, input().split()))
max_hight = hights[0]
for i in range(1, num_of_buildings):
    if hights[i] > max_hight:
        print(i+1)
        break
else:
    print('-1')