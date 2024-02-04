num_of_heros = int(input())
num_of_monsters = list(map(int, input().split()))
num_of_powers = [0] + list(map(int, input().split()))
beated_monsters = 0
remain_power = 0
for monsters, power in zip(num_of_monsters[::-1], num_of_powers[::-1]):
    # 一個前の残りを処理
    if monsters > remain_power:
        beated_monsters += remain_power
        monsters = monsters - remain_power
    else:
        beated_monsters += monsters
        monsters = 0
    
    #今回分を処理
    if monsters > power:
        beated_monsters += power
        remain_power = 0
    else:
        beated_monsters += monsters
        remain_power = power - monsters
        
print(beated_monsters)
    