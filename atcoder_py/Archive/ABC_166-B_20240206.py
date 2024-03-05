num_of_people, num_of_sweets = map(int, input().split())
have_sweets = set()
for i in range(num_of_sweets):
    _ = input()
    for j in list(map(int, input().split())):
        have_sweets.add(j)

print(num_of_people - len(have_sweets))