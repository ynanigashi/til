_ = input()
lengths = list(map(int, input().split()))
max_length = max(lengths)
print('Yes' 
      if sum(lengths) - max_length > max_length 
      else 'No')
