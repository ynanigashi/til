prices = list(map(int, input().split()))
sorted_prices = sorted(prices)
print(sum(sorted_prices[:2]))