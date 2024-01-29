(range_of_balls, 
 num_of_blue_balls, 
 num_of_red_balls) = map(int, input().split())
patern_in_range, remainder = divmod(range_of_balls, num_of_blue_balls + num_of_red_balls)
blue_balls_in_range = patern_in_range * num_of_blue_balls
blue_balls_in_range += min(remainder, num_of_blue_balls)

print(blue_balls_in_range)