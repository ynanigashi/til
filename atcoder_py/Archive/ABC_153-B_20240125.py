hit_point, _ = map(int, input().split())
attacks = list(map(int, input().split()))
print('Yes' if hit_point <= sum(attacks) else 'No')