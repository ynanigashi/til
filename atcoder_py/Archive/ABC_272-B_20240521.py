num_of_person, num_of_party = map(int, input().split())
parties = []
for _ in range(num_of_party):
    menbers = list(map(int, input().split()))
    members_set = set(menbers[1:])
    parties.append(members_set)

break_flag = False
for i in range(1, num_of_person+1):
    for j in range(i+1, num_of_person+1):
        same_flag = False
        for party in parties:
            if i in party and j in party:
                same_flag = True
                break

        if not same_flag:
            break_flag = True
            break

    if break_flag:
        break
else:
    print('Yes')
    exit()

print('No')