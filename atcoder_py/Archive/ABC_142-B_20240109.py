num_of_people, min_hight = map(int, input().split())
hights = list(map(int, input().split()))
for hight in hights:
    if hight < min_hight:
        num_of_people -= 1
print(num_of_people)