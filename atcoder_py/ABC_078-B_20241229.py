(width_of_chair, 
 width_of_man, 
 width_of_space) = map(int, input().split())

num_of_man, remainder = divmod(width_of_chair, 
                             (width_of_man + width_of_space))

print(
    num_of_man if remainder >= width_of_space
    else num_of_man - 1
    )