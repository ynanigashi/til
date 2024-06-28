_, defalut_price, base_price = map(int, input().split())
prices = list(map(lambda x: int(x)+base_price, input().split()))
prices.append(defalut_price)
print(min(prices))