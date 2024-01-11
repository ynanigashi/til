num_of_takoyakis = int(input())
takoyakis = list(map(int, input().split()))
recovery_points = 0
for i in range(num_of_takoyakis):
    for j in range(i + 1, num_of_takoyakis):
        recovery_points += takoyakis[i] * takoyakis[j]
print(recovery_points)