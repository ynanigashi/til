n = int(input())
points = sorted(list(map(int, input().split())))
len_points = len(points)
print(sum(points[n:len_points - n])/ (len_points - 2 * n))