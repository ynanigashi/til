num_of_stones = int(input())
color_of_stones = input()
cnt = [0 for _ in range(num_of_stones)]
red = 0

# 赤石の数をカウント
for i in range(num_of_stones):
    if color_of_stones[i] == 'R':
        red += 1
    cnt[i] = red

# 赤石の数から赤石にしなくてもいい石の数を引く = 赤石にする必要のある石の数
print(red - cnt[red-1])