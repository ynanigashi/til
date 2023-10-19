n, y = map(int, input().split())
a, b, c = -1, -1, -1
i_max = min(n, y//10000)
for i in range(i_max+1):
    j_max = min(n-i, (y-i*10000)//5000)
    for j in range(j_max + 1):
        k = n - (i+j)
        if i*10000+j*5000+k*1000 == y:
            a, b, c = i, j, k
            break
    if a != -1: break

print('{} {} {}'.format(a, b, c))
