num_of_people, train_fare, taxi_fare = map(int, input().split())
print(min(num_of_people * train_fare, taxi_fare))