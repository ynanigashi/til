num_of_magics, time_limit, damage_limit = map(int, input().split())
for _ in range(num_of_magics):
    magic_time, magic_damage = map(int, input().split())
    if magic_time < time_limit and magic_damage > damage_limit:
        print('Yes')
        break
else:
    print('No')