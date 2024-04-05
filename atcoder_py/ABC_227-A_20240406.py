(num_of_people, 
 num_of_cards, 
 start_person) = map(int, input().split())
answer = (start_person + num_of_cards - 1) % num_of_people
print(answer if answer != 0 else num_of_people)