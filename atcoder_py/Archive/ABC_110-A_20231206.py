numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
print(numbers[0] * 10 + numbers[1] + numbers[2])