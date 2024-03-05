num_of_sheep, num_of_wolves = map(int, input().split())
print('unsafe' if num_of_sheep <= num_of_wolves else 'safe')