numbers = list(map(int, input().split()))
num_of_times = int(input())
numbers.sort(reverse=True)

for _ in range(num_of_times):
    numbers[0] *= 2

print(sum(numbers))