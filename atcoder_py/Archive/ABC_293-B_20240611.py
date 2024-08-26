num_of_people = int(input())
people = list(map(int, input().split()))
called_people = set()
for i in range(num_of_people):
    if i + 1 in called_people:
        continue
    called_people.add(people[i])

answer = list(set(range(1, num_of_people+1)) - called_people)
print(len(answer))
print(*answer)
