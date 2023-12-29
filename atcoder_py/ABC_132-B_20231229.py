len_of_nums = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in range(len_of_nums-2):
    if nums[i] < nums[i+1] < nums[i+2] or nums[i] > nums[i+1] > nums[i+2]:
        cnt += 1
print(cnt)