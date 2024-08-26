single_value, set_value, num_of_apples = map(int, input().split())
set_value_min = set_value*(num_of_apples//3)+single_value*(num_of_apples%3)
single_value_min = single_value*num_of_apples
print(min(set_value_min, single_value_min))