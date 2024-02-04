num_of_coords, dimension = map(int, input().split())
coords = [list(map(int, input().split())) for _ in range(num_of_coords)] # 2次元配列
ans = 0
for i in range(num_of_coords):
    for j in range(i+1, num_of_coords):
        tmp = 0
        for k in range(dimension):
            tmp += (coords[i][k] - coords[j][k])**2
        if tmp**0.5 == int(tmp**0.5):
            ans += 1
print(ans)