a = list(map(int, input().split()))
print("YES" if a.count(5) == 2 and a.count(7) == 1 else "NO")