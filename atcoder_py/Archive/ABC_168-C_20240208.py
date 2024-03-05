import math
(length_of_hour_hand, 
 length_of_minute_hand, 
 hour, 
 minute) = map(int, input().split())
hour_angle = 30 * hour + 0.5 * minute
minute_angle = 6 * minute
rad = math.radians(abs(hour_angle - minute_angle))
# 余弦定理
# a^2 = b^2 + c^2 - 2bc * cosA
ans = math.sqrt(length_of_hour_hand ** 2 + length_of_minute_hand ** 2 - 2 * length_of_hour_hand * length_of_minute_hand * math.cos(rad))
print(ans)