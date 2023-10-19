_ = int(input())
a = list(map(int, input().split()))
cnt = 0

while True:
    is_even = []
    for i, j in enumerate(a):
        is_even.append(j%2 == 0)
        a[i] = j//2
    
    if all(is_even) == False:break

    cnt += 1

print(cnt)