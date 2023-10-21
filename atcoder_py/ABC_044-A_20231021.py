total_days, full_price_days, full_price, discounted_price = [int(input()) for i in range(4)]
default_prise = total_days * full_price
discounted_days = total_days - full_price_days if total_days - full_price_days >= 0 else 0
price_gap = full_price - discounted_price
accommodation_fee = default_prise - (price_gap * discounted_days)
print(accommodation_fee)