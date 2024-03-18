num_of_dises, target_num = map(int, input().split())
print('Yes' if num_of_dises <= target_num <=num_of_dises * 6 else 'No')