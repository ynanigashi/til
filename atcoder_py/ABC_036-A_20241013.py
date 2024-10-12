from math import ceil 
num_of_bottles, limit = map(int, input().split())
print(ceil(limit / num_of_bottles))