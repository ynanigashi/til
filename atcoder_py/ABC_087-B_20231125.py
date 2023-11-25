y500, y100, y50, price = [int(input()) for _ in range(4)]
cnt = 0
for i in range(y500+1):
    if i*500 > price:
        break
    for j in range(y100+1):
        if i*500+j*100 > price:
            break
        for k in range(y50+1):
            if i*500+j*100+k*50 > price:
                break
            elif i*500+j*100+k*50 == price:
                cnt += 1
print(cnt)