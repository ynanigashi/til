numbers = tuple(int(i) for i in input())
answer = 19

# bit全探索
for i in range(2 ** len(numbers)):
    count = 0
    sum_of_numbers = 0 
    for j in range(len(numbers)):
        if (i >> j) & 1:
            sum_of_numbers += numbers[j]
        else:
            count += 1
    if sum_of_numbers != 0 and sum_of_numbers % 3 == 0:
        answer = min(answer, count)

print(answer if answer != 19 else -1)