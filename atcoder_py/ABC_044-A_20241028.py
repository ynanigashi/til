num_of_days = int(input())
limit_days = int(input())
defaul_price = int(input())
discount_price = int(input())
if num_of_days <= limit_days:
    print(num_of_days * defaul_price)
else:
    print(limit_days * defaul_price + (num_of_days - limit_days) * discount_price)