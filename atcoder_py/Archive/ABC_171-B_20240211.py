num_of_fruits, num_of_fruits_to_buy = map(int, input().split())
fruits_prices = list(map(int, input().split()))
fruits_prices.sort()
print(sum(fruits_prices[:num_of_fruits_to_buy]))