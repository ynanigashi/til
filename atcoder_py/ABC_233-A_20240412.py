import math
stamp_value, target_value = map(int, input().split())
print(max(math.ceil((target_value - stamp_value)/10),0))