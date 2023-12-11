num_of_presents = int(input())
prices = [int(input()) for _ in range(num_of_presents)]
print(sum(prices) - max(prices) // 2)