from collections import Counter
num_of_candies, quantity = map(int, input().split())
candies = list(map(int, input().split()))
# 範囲内の種類数を求める
candy_counter = Counter(candies[:quantity])
max_candy = len(candy_counter)

# 範囲をずらしながら種類数を求める
for i in range(quantity, num_of_candies):
    # 種類数を更新、追加
    candy_counter[candies[i]] += 1
    candy_counter[candies[i - quantity]] -= 1
    # 種類数が0になったら削除
    if candy_counter[candies[i - quantity]] == 0:
        candy_counter.pop(candies[i - quantity])
    max_candy = max(max_candy, len(candy_counter))

print(max_candy)