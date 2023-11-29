tasks = list(map(int, input().split()))
tasks.sort()
print(tasks[1]-tasks[0]+tasks[2]-tasks[1])