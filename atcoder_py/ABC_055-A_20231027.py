reward_threshold = 15
value = 800
reward_point = 200
eating_cnt = int(input())
reward_cnt = eating_cnt // reward_threshold
print(eating_cnt * value - reward_cnt * reward_point)
