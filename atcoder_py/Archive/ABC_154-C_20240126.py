len_of_nums = int(input())
nums = list(map(int, input().split()))
print('YES' if len(set(nums)) == len_of_nums else 'NO')