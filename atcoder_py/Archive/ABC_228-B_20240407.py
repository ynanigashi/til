num_of_friends, start_friend = map(int, input().split())
friends = list(map(int, input().split()))
count = 0
while True:
    temp = start_friend - 1
    if friends[temp] == 0:
        break
    count += 1
    start_friend = friends[temp]
    friends[temp] = 0

print(count)