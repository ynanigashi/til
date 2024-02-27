num_of_people = 2**int(input())
people = list(map(int, input().split()))
center = num_of_people // 2
seconds = min(max(people[:center]), max(people[center:]))
print(people.index(seconds) + 1)