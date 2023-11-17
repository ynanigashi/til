(width_of_chair, 
 width_of_man, 
 width_of_space) = map(int, input().split())

width_of_chair -= width_of_space
print(width_of_chair//(width_of_man+width_of_space))