num_of_pastas, num_of_days = map(int, input().split())
pastas = list(map(int, input().split()))
days = list(map(int, input().split()))
classfied_pastas = {}
for pasta in pastas:
    if pasta not in classfied_pastas:
        classfied_pastas[pasta] = 1
    else:
        classfied_pastas[pasta] += 1

for day in days:
    if day in classfied_pastas:
        classfied_pastas[day] -= 1
        if classfied_pastas[day] == 0:
            classfied_pastas.pop(day)
    else:
        print('No')
        break
else:
    print('Yes')