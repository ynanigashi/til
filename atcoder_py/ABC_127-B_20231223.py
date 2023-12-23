rate, subtract, grams = map(int, input().split())
for _ in range(10):
    grams = grams * rate - subtract
    print(grams)
