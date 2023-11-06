hours, per_yen, price_b = map(int, input().split())
price_a = hours * per_yen
print(price_a if price_a < price_b else price_b)