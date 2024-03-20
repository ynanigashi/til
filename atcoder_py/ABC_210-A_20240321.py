(quantities, 
 discont_threshold, 
 price, 
 discount_price) = map(int, input().split())
answer = min(quantities, discont_threshold) * price + max(0, quantities - discont_threshold) * discount_price
print(answer)