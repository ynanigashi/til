n = int(input())
a = list(map(int, input().split()))

# マイナスの数を取得
num_nimus = sum(i < 0 for i in a)

# 全部＋に出来た場合の合計を取得
abs_sum_a = sum(map(abs, a))
# 最小の値を取得
min_abs_a = min(map(abs, a))

if num_nimus % 2 == 0:
    # マイナスの数が偶数の場合すべての数をプラスに変換できる
    ans = abs_sum_a
else:
    # そうでない場合は、1つがマイナスになるので最小の値をマイナスにした合計を算出
    ans = abs_sum_a - min_abs_a*2

print(ans)