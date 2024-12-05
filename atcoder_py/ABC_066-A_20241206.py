prices = list(map(int, input().split()))
prices.sort()
print(prices[0] + prices[1])