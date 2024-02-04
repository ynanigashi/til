# 標準入力からデスクの幅と二つのデスクの位置を読み込む
desk_width, position_a, position_b = map(int, input().split())

# 二つのデスクの位置を比較して、それぞれの最大値と最小値を求める
farthest_desk = max(position_a, position_b)
nearest_desk = min(position_a, position_b)

# 最も近いデスクの終端から最も遠いデスクの開始までの距離を計算
distance_between_desks = farthest_desk - (nearest_desk + desk_width)

# デスクが重なっているか接触している場合、距離は0になる
distance = max(0, distance_between_desks)

# 計算した距離を出力
print(distance)