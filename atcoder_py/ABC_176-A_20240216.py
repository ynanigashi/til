import math
(num_of_takoyaki,
 num_of_takoyaki_per_turn, 
 minutes,
 ) = map(int, input().split())

print(math.ceil(num_of_takoyaki / num_of_takoyaki_per_turn) * minutes)