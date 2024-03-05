import math
t_hp, t_atk, a_hp, a_atk = map(int, input().split())
t_atk_count = math.ceil(a_hp / t_atk)
a_atk_count = math.ceil(t_hp / a_atk)
print('Yes' if t_atk_count <= a_atk_count else 'No')