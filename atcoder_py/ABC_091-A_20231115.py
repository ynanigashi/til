a_coin, b_coin, price = map(int, input().split())
print('Yes' if a_coin + b_coin >= price else 'No')