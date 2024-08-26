len_of_seq, total = map(int, input().split())
seq = list(map(int, input().split()))
ans = 0
for i in seq:
    total -= i
    if total >= 0:
        ans += 1
    else:
        break
print(ans)
