len_of_nums = int(input())
nums = list(map(int, input().split()))
temp = 0
for i in nums:
    print(i - temp, end=' ')
    temp = i