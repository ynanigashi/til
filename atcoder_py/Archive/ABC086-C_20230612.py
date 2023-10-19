n = int(input())

# 前回の値を保持
pt, px, py = 0, 0, 0
ans = 'No'
for _ in range(n):
    ct, cx, cy = map(int, input().split())
    
    # 差分を取る
    t, x, y = ct-pt, abs(cx-px), abs(cy-py)

    # 時間が足りない場合はたどり着けない
    if t < x + y: break

    # パリティが合わない場合はたどり着けない
    if t%2 != (x+y)%2: break

    # 前回の値を置き換える
    pt, px, py = ct, cx, cy
    
else:
    ans = 'Yes'

print(ans)