from math import ceil
num_of_apple_trees, distance = map(int, input().split())
print(ceil(num_of_apple_trees/(distance*2+1)))