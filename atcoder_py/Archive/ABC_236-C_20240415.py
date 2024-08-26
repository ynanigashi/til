(num_of_stations, 
 num_of_stop_stations) = map(int, input().split())
stations = list(input().split())
num_of_stop_stations = set(input().split())

for station in stations:
    if station in num_of_stop_stations:
        print('Yes')
    else:
        print('No')
