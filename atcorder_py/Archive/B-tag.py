import math
A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
#二人の距離
D = abs(A - B)
#時間内に縮められる距離＝（１秒間に縮まる距離）*制限時間
D2 = (V - W) * T
#縮められる距離が二人の距離よりも大きい場合は捕まえられる
print("YES" if D <= D2 else "NO")