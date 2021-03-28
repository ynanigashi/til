import numpy as np
# 平面上の任意の点の回転関数
# qに軸の座標を指定
# pに回転させたい点の座標を指定
# tに回転角を指定
def rotation(xy, r_axis, t, deg=False):
 
    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)
 
    xy = np.array(xy)
    r_axis = np.array(r_axis)
 
    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
 
    return  np.dot(R, xy - r_axis) + r_axis
 
n = int(input())
x0, y0 = map(int, input().split())
x_opo, y_opo = map(int, input().split())
 
q = (x0,y0)
p = ((x0+x_opo)/2,(y0+y_opo)/2)
 
q = rotation(q, p, np.pi/(n/2))
print("{} {}".format(q[0], q[1]))