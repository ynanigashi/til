num_of_impute = int(input())
city_population = {}
population_sum = 0
max_population = 0
for _ in range(num_of_impute):
    city, population = input().split()
    population = int(population)
    city_population[population] = city
    
    population_sum += population
    max_population = max(max_population, population)

if max_population > population_sum / 2:
    print(city_population[max_population])
else:
    print('atcoder')