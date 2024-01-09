num_of_people = int(input())
students = list(map(int, input().split()))

for index, student in enumerate(students):
    students[index] = [index + 1, student]

students.sort(key=lambda x: x[1])

print(' '.join([str(student[0]) for student in students]))