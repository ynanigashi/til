minimum, maximum, target = map(int, input().split())
include_num = set()
for i in range(minimum, min(minimum+target, maximum+1)):
    include_num.add(i)
for i in range(max(maximum-target+1, minimum), maximum+1):
    include_num.add(i)

include_num = sorted(include_num)
for i in include_num:
    print(i)