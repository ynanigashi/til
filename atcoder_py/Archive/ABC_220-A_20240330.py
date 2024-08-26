import math
min_num, max_num, multiple = map(int, input().split())
answer = math.ceil(min_num / multiple) * multiple
print(answer if answer <= max_num else -1)