target, start, end = map(int, input().split())
if start < end:
    print('No' if start < target < end else 'Yes')
else:
    print('Yes' if end < target < start else 'No')