hight, _ = map(int, input().split())
cnt = 0
for _ in range(hight):
    s = input()
    cnt += s.count('#')

print(cnt)