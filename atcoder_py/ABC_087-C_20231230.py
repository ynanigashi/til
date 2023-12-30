num_of_cells = int(input())
upper_cells = list(map(int, input().split()))
lower_cells = list(map(int, input().split()))
candies = upper_cells[0] + lower_cells[-1]
for i in range(num_of_cells):
    upper_way = sum(upper_cells[i+1:])
    lower_way = sum(lower_cells[i:]) - lower_cells[-1]
    if upper_way > lower_way:
        candies += upper_cells[i+1]
    else:
        candies += lower_way
        break
print(candies) 