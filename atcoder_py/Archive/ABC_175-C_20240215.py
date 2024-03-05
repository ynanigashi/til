coordinate, turns, distance = map(int, input().split())

# 移動距離が初期地点から0までの距離より短い場合
if coordinate >= turns * distance:
    print(coordinate - turns * distance)
    exit()

# 移動距離が初期地点から0までの距離より長い場合
close_turn = coordinate // distance

# もっとも近づける距離と、そのターン数を求める
if coordinate - close_turn * distance < abs(coordinate - (close_turn + 1) * distance):
    min_distance = coordinate - close_turn * distance
else:
    min_distance = abs(coordinate - (close_turn + 1) * distance)
    close_turn += 1

turns -= close_turn

# ターン数が偶数の場合、もっとも近づける距離を出力
# ターン数が奇数の場合、もっとも近づける距離からもう一ターン進んだ距離を出力
print(min_distance if turns % 2 == 0 else distance - min_distance)