(num_of_people,
 start_point,
 num_of_questions) = map(int, input().split())
points = [start_point - num_of_questions] * num_of_people

for _ in range(num_of_questions):
      winner = int(input()) - 1
      points[winner] += 1

for point in points:
      print('Yes' if point > 0 else 'No')