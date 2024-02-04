sec_of_round, num_of_biscuits, sec_of_time = map(int, input().split())
print(sec_of_time // sec_of_round * num_of_biscuits)