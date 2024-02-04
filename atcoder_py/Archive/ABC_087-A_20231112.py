money, cake_price, donut_price = [
    int(input())
    for _ in range(3)
    ]
print((money - cake_price)%donut_price)