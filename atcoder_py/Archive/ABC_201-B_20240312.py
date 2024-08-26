num_of_moutains = int(input())
mountains = []
for _ in range(num_of_moutains):
    name, height = input().split()
    mountains.append((name, int(height)))

mountains.sort(key=lambda x: x[1], reverse=True)
second_highest_mountain_name = mountains[1][0]
print(second_highest_mountain_name)