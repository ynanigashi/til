num, cardinal_num = map(int, input().split())
cnt = 0
while num > 0:
      num //= cardinal_num
      cnt += 1
print(cnt)