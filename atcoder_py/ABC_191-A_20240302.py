mps, min_sec, max_sec, distance = map(int, input().split())
vanish_point = distance / mps
if min_sec <= vanish_point <= max_sec:
    print('No')
else:
    print('Yes')