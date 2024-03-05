max_battery, num_of_caffes, home_arrive_hour = map(int, input().split())
caffes = [tuple(map(int, input().split())) for _ in range(num_of_caffes)]
caffes.append((home_arrive_hour, home_arrive_hour))
leave_hour = 0
battery = max_battery
for start_hour, end_hour in caffes:
    battery -=  start_hour - leave_hour
    if battery <= 0:
        print('No')
        break
    battery = min(battery + end_hour - start_hour, max_battery)
    leave_hour = end_hour
else:
    print('Yes')