num_of_rice_cakes, num_of_people = map(int, input().split())
print(0 if num_of_rice_cakes % num_of_people == 0 else 1)
