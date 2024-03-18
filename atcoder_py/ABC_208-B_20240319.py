coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
target_num = int(input())
answer = 0
for coin in coins[::-1]:
        div_num, target_num = divmod(target_num, coin) 
        answer += div_num

print(answer)