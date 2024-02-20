num_of_inputs = int(input())
sum = 0
for i in range(num_of_inputs):
    a, b = map(int, input().split())
    sum += (b - a + 1) * (a + b) // 2

print(sum)