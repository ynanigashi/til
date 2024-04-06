on_hour, off_hour, target_hour = map(int, input().split())
answer = 'No'
if on_hour <= target_hour < off_hour:
    answer = 'Yes'
elif off_hour < on_hour:
    if on_hour <= target_hour or target_hour < off_hour:
        answer = 'Yes'

print(answer)