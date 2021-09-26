n = int(input())
t = 0
d = 0
while(True):
    d += 1
    t = (d*d + d)/2
    if t >= n:
        break
print(d)