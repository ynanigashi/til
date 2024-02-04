(num_of_boxies,
 num_of_toll_booths,
 start_coordinate) = map(int, input().split())
toll_booth_coordinates = list(map(int, input().split()))
passed_toll_booths = 0
for i in range(start_coordinate+1):
    if i in toll_booth_coordinates:
        passed_toll_booths += 1

print(min(passed_toll_booths, num_of_toll_booths-passed_toll_booths))