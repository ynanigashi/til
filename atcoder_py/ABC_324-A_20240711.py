_ = input()
nums = list(map(int, input().split()))
print('Yes' if len(set(nums)) == 1 else 'No')