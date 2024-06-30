n = int(input())
people = list(map(int, input().split()))
max_power = max(people[1:])
me = people[0]
if me > max_power:
    ans = 0
else:
    ans = max_power - me + 1

print(ans)