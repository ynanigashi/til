num_of_foods, num_of_dislikes = map(int, input().split())
foods = list(map(int, input().split()))
dislikes = list(map(int, input().split()))
dislikes = [foods[i - 1] for i in dislikes]
most_delicious = max(foods)

print('Yes' if most_delicious in dislikes else 'No')