num_of_questions, points = map(int, input().split())
questions = input()
for question in questions:
    if question == "o":
        points += 1
    else:
        points = max(0, points-1)

print(points)