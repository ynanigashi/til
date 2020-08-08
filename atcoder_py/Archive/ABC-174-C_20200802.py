k = int(input())
if k%2 == 0:
    print(-1)
else:
    i, j, cnt = 0, 1, 1
    while True:
        i = (i + j) * 7
        if i%k == 0:
            break
        i = int(i)//7
        j *= 10
        cnt += 1
    print(cnt)