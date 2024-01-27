len_of_nums = int(input())
nums = list(map(int, input().split()))
nums = [i for i in nums if i % 2 == 0]
filterd_nums = [i for i in nums if i % 3 == 0 or i % 5 == 0]
print('APPROVED' if len(nums) == len(filterd_nums) else 'DENIED')