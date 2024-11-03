candies = sorted(list(map(int, input().split())))
print('Yes' if candies[0] + candies[1] == candies[2] else 'No')