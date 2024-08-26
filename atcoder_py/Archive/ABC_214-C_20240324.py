num_of_people = int(input())
waiting_times = list(map(int, input().split()))
times = list(map(int, input().split()))
for i in range(num_of_people*2):
    times[(i+1)%num_of_people] = min(times[(i+1)%num_of_people], 
                                          times[i%num_of_people] + waiting_times[i%num_of_people])

for time in times:
    print(time)