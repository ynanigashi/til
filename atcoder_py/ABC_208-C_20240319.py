num_of_people, num_of_sweets = map(int, input().split())
people_numbers = list(map(int, input().split()))
sorted_people_numbers = sorted(people_numbers)
min_sweets = num_of_sweets // num_of_people
remaining_sweets = num_of_sweets % num_of_people
last_person = sorted_people_numbers[remaining_sweets - 1] if remaining_sweets > 0 else -1
for i in range(num_of_people):
    print(min_sweets + (1 if sorted_people_numbers[i] <= last_person else 0))
