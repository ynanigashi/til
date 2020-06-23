import math
X, N = map(int, input().split())
p_list = list(map(int, input().split()))
ans = p_list[0]

def near_num(a, b):
    global X
    if abs(X-a) < abs(X-b):
        return a
    elif abs(X-a) > abs(X-b):
        return b
    else:
        return a if a < b else b

for i in p_list[0:]:
    ans = near_num(ans, i)

print(ans)
