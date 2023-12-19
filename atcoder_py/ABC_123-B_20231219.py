wait_times = [int(input()) for _ in range(5)]
wait_times.sort(key=lambda x: 10 if x % 10 == 0 else x % 10)
print(sum(
    [wait_time + (10 - wait_time % 10) 
     if wait_time % 10 != 0 
     else wait_time 
     for wait_time in wait_times[1:]]
     ) 
     + wait_times[0]
     )
