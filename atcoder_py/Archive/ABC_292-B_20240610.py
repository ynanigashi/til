num_of_players, num_of_queries = map(int, input().split())
players = [{'red': 0, 'yellow': 0} for _ in range(num_of_players)]
for _ in range(num_of_queries):
    query = list(map(int, input().split()))
    if query[0] == 1:
        players[query[1] - 1]['yellow'] += 1
    elif query[0] == 2:
        players[query[1] - 1]['red'] += 1
    else:
        if players[query[1] - 1]['yellow'] > 1 or players[query[1] - 1]['red'] > 0:
            print('Yes')
        else:
            print('No')