num_of_inputs = int(input())
inputs = list(list(map(int, input().split())) for _ in range(num_of_inputs))
left_num, right_num = 0, 0
for type, left, right in inputs:
    if type == 2:
        right -= 1
    if type == 3:
        left += 1
    if type == 4:
        right -= 1
        left += 1

    left_num = max(left_num, left)
    right_num = min(right_num, right)

print(right_num - left_num + 1 
      if right_num - left_num >= 0 else 0)

#何かを勘違いしたらしい