num_of_rooms, num_of_plus_rooms, time = map(int, input().split())
wait_time = list(map(int, input().split()))
wait_time.insert(0, 0)
plus_rooms = {}
for _ in range(num_of_plus_rooms):
    room_number, time = map(int, input().split())
    plus_rooms[room_number] = time

for i in range(num_of_rooms):
    if time < wait_time[i]:
        print('No')
        break
    if i in plus_rooms:
        diff = wait_time[i] - plus_rooms[i]
        time -= diff
    else:
        time -= wait_time[i]
    
else:
    print('Yes')
