remain_of_a, remain_of_b = map(int, input().split())
coordinate_of_a = remain_of_b - remain_of_a
print(sum(range(coordinate_of_a)) - remain_of_a)