num_of_items, money = map(int, input().split())
prices = list(map(int, input().split()))
discounted_prices = [price - (i % 2) * 1 for i, price in enumerate(prices)]
print('Yes' if sum(discounted_prices) <= money else 'No')