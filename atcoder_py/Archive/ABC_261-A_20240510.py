l1, r1, l2, r2 = map(int, input().split())
set1 = set(range(l1, r1+1))
set2 = set(range(l2, r2+1))
print(max(len(list(set1 & set2))-1, 0))