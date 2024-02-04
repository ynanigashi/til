a, b, c = map(int, input().split())
numbers = [a, b, c]

if numbers.count(5)==2 and numbers.count(7)==1:
    print('YES')
else:
    print('NO')