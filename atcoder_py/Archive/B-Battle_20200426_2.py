t_hp, t_atk, a_hp, a_atk = map(int, input().split())
t_life_span = -(-t_hp//a_atk)
a_life_span = -(-a_hp//t_atk)
print("Yes" if t_life_span >= a_life_span else "No")