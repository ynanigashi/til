num_of_shops = int(input())
shops  = [list(map(int, input().split())) for _ in range(num_of_shops)]
can_buy_list = [shop[1] for shop in shops if shop[0] < shop[2]]
print(min(can_buy_list) if can_buy_list else -1)