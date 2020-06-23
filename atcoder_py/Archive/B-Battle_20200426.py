t_hp, t_atk, a_hp, a_atk = map(int, input().split())
while True:
    a_hp -= t_atk
    if a_hp <= 0: break
    t_hp -= a_atk
    if t_hp <= 0: break
print("Yes" if t_hp > 0 else "No")