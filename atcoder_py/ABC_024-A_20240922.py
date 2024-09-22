kids_fee, adult_fee, discount, min_limit = map(int, input().split())
kids_num, adult_num = map(int, input().split())
total_fee = kids_fee * kids_num + adult_fee * adult_num
total_num = kids_num + adult_num
if total_num >= min_limit:
    total_fee -= total_num * discount

print(total_fee)