num_of_cups, max_milliliters = map(int, input().split())
alcohol_ml = 0
for i in range(num_of_cups):
    milliliters, percent = map(int, input().split())
    alcohol_ml += milliliters * percent
    if alcohol_ml > max_milliliters*100:
        print(i + 1)
        break
else:
    print(-1)