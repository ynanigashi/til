num_of_monsters, num_of_attacks = map(int, input().split())
monsters = list(map(int, input().split()))
monsters.sort(reverse=True)
print(sum(monsters[num_of_attacks:])
      if num_of_attacks <= num_of_monsters 
      else 0)