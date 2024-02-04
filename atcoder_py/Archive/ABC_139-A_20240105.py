forcast = input()
weather = input()
cnt = 0
for i in range(3):
    if forcast[i] == weather[i]:
        cnt += 1
print(cnt)