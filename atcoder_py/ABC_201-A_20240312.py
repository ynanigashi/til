numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
diff_ab = sorted_numbers[1] - sorted_numbers[0]
diff_bc = sorted_numbers[2] - sorted_numbers[1]
print('Yes' if diff_ab == diff_bc else 'No')