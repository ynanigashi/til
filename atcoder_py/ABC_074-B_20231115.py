num_of_input = int(input())
robot_b = int(input())
coordinates = list(map(int, input().split()))
ans = 0
for i in coordinates:
    ans += min(i, robot_b - i)
print(ans * 2)