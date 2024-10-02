hour, minuite = map(int, input().split())
hour_angle = 30 * (hour%12) + 0.5 * minuite
minuite_angle = 6 * minuite
angle = abs(hour_angle - minuite_angle)
angle = min(angle, 360 - angle)
print(angle)