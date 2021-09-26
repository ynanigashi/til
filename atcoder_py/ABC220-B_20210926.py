def to_int(s, k):
    res, i = 0, 0
    for c in s:
        res += int(c) * (k**i)
        i += 1
    return res

k = int(input())
a, b = map(lambda s: str(s)[::-1], input().split())
print(to_int(a, k)*to_int(b, k))
