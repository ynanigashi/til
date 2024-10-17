h1, w1 = map(int, input().split())
h2, w2 = map(int, input().split())
hw2 = (h2, w2)
if h1 in hw2 or w1 in hw2:
    print("YES")
else:
    print("NO")