num_of_people = int(input())
name, age = [], []
for _ in range(num_of_people):
    n, a = input().split()
    name.append(n)
    age.append(int(a))

min_age = min(age)
min_age_index = age.index(min_age)

output_order = [i%num_of_people for i in range(min_age_index, num_of_people+min_age_index)]

for i in output_order:
    print(name[i])