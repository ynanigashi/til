num_of_cels = int(input())
cels = list(map(int, input().split()))
cnt, cnt_max = 0, 0
for i in range(num_of_cels-1):
    if cels[i] >= cels[i+1]:
        cnt += 1
    else:
        cnt = 0
    
    cnt_max = max(cnt, cnt_max)
print(cnt_max)