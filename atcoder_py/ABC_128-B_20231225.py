num_of_restaurants = int(input())
restaurants = []

for i in range(1, num_of_restaurants + 1):
    city, score = input().split()
    restaurants.append({'city': city, 'score': int(score), 'index': i})

restaurants.sort(key=lambda x: (x['city'], -x['score']))

for restaurant in restaurants:
    print(restaurant['index'])