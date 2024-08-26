num_of_students, min_limit = map(int, input().split())
students = list(map(int, input().split()))
count = 0
for student in students:
    if student < min_limit:
        count += 1

print(count)