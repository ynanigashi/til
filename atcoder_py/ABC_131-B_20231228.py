num_of_apples, taste = map(int, input().split())
taste_of_apples = [taste+i for i in range(num_of_apples)]
taste_of_apples.sort(key=lambda x: abs(x))
print(sum(taste_of_apples[1:]))