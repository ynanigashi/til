num_of_people = int(input())
people = [list(input().split()) for _ in range(num_of_people)]
for i in range(num_of_people):
    surname_duplicate = False
    givenname_duplicate = False
    for j in range(num_of_people):
        if i == j:
            continue
        if people[i][0] in people[j]:
            surname_duplicate = True
        if people[i][1] in people[j]:
            givenname_duplicate = True
        
    if surname_duplicate and givenname_duplicate:
        print('No')
        break
else:
    print('Yes')