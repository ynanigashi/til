num_of_floors, num_of_rooms = map(int, input().split())
answer = int((num_of_floors + 1)*num_of_floors/2 * num_of_rooms * 100 
      + num_of_floors * (num_of_rooms + 1)*num_of_rooms/2)
print(answer)