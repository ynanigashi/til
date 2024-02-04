train_fee_a, train_fee_b, bus_fee_a, bus_fee_b = [int(input()) for _ in range(4)]
print(min(train_fee_a, train_fee_b) + min(bus_fee_a, bus_fee_b))