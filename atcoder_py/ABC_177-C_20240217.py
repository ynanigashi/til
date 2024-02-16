num_of_numbers = int(input())
numbers = list(map(int, input().split()))
mod = 10**9 + 7

sum = sum(numbers)
answer = 0

for i in numbers:
    sum -= i
    answer += i * sum
    answer %= mod

print(answer)