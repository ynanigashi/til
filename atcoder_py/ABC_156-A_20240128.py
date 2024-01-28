num_of_contests, rate = map(int, input().split())
print(rate 
      if num_of_contests >= 10 
      else rate + 100 * (10 - num_of_contests))