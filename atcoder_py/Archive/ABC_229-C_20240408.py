num_of_cheese, limit_weight = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(num_of_cheese)]
cheeses.sort(key=lambda x: x[0], reverse=True)
total_deliciousness = 0

for cheese in cheeses:
    delicious, weight = cheese
    if limit_weight - weight >= 0:
        total_deliciousness += delicious * weight
        limit_weight -= weight
    else:
        total_deliciousness += delicious * limit_weight
        break

print(total_deliciousness)
