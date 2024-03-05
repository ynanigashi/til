num_people = int(input())
people = list(map(int, input().split()))
current_height = 0
box_height = 0
for person in people:
    if person < current_height:
        box_height += current_height - person
    else:
        current_height = person

print(box_height)