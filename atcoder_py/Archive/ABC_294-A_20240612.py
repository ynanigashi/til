_ = input()
nums = list(map(int, input().split()))
nums = [i for i in nums if i % 2 == 0]
print(*nums)