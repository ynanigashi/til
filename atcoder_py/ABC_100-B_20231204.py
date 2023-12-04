d, n = map(int, input().split())
#100の場合は割り切れる数字になるので１を足す
print((100 ** d) * (n + (n == 100)))