num_of_contestants, num_of_inputs = map(int,input().split())
points = [0] * num_of_contestants
diff = 1
for _ in range(num_of_inputs):
    contestant, point = map(int, input().split())
    before_point = points[contestant-1]
    after_point = before_point + point

    if after_point not in points:
        diff += 1
    
    points[contestant-1] = after_point

    if before_point not in points:
        diff -= 1

    print(diff)