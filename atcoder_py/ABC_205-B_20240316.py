len_of_numbers = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
for i in range(len_of_numbers):
    if numbers[i] != i + 1:
        print("No")
        break
else:
    print("Yes")