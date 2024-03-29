len_of_nums = int(input())
nums = list(map(int, input().split()))
target = int(input())
sum_of_nums = sum(nums)
quotient = target // sum_of_nums
remainder = target % sum_of_nums
answer = quotient * len_of_nums
if remainder == 0:
    print(answer)
    exit()

for num in nums:
    answer += 1
    remainder -= num
    if remainder <= 0:
        break
print(answer)