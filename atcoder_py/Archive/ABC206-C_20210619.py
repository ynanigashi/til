import itertools
n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt, i, dupulicate  = 0, 0, 1
while(i < n - 1):
    if a[i] == a[i+1]:
        dupulicate += 1
    else:
        cnt += (n - i - 1)*dupulicate
        dupulicate = 1
    i += 1
print(cnt)