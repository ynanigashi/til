X, Y = map(int, input().split())
turu_kame = []
if Y%2 == 0: 
    for i in range(Y//4+1):
        turu_kame.append(int(i+(Y-i*4)/2))
print("Yes" if X in turu_kame else "No")