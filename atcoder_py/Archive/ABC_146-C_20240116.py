#　急に難易度タカシ
a, b, x = map(int, input().split())

left = 0
right = 10**9+1

while left + 1 < right:
    # 二分探索範囲の中央値をmidとする
    mid = left + (right - left) // 2
    # 以下の条件に合致していればleftをmidに持ってくる
    # midの右側に、そうでなければ左側を処理する
    if a * mid + b * len(str(mid)) <= x:
        left = mid
    else:
        right = mid


print(left)