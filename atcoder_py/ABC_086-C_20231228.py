num_of_inputs = int(input())
x_coord, y_coord, time = 0, 0, 0
ans = 'Yes'

# 入力された回数分、座標と時間を更新しながらループを行う
for _ in range(num_of_inputs):
    t, x, y = map(int, input().split())
    x_move, y_move = abs(x-x_coord), abs(y-y_coord)

    # 移動距離が経過時間よりも大きい場合、'No'を代入
    if x_move + y_move > t - time:
        ans = 'No'
        break
    # 移動距離と経過時間の偶奇が一致しない場合、'No'を代入
    elif (x_move + y_move) % 2 != (t - time) % 2:
        ans = 'No'
        break    
    # 座標と時間を更新
    x_coord, y_coord, time = x, y, t

print(ans)