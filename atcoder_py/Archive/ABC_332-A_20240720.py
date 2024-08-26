num_of_inputs, min_price, send_fee = map(int, input().split())
total_price = 0
for _ in range(num_of_inputs):
    price, quantity = map(int, input().split())
    total_price += price * quantity

print(total_price if total_price >= min_price else total_price + send_fee)