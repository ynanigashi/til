num_of_people, num_of_foods = map(int, input().split())
foods = {i for i in range(1, num_of_foods+1)}
for _ in range(num_of_people):
    _, *food = map(int, input().split())
    foods &= set(food)
print(len(foods))