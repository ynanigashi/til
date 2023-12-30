num_of_cells = int(input())
upper_cells = list(map(int, input().split()))
lower_cells = list(map(int, input().split()))
ans = []
for i in range(num_of_cells):
    upper_sum = sum(upper_cells[:i+1])
    lower_sum = sum(lower_cells[i:])
    ans.append(upper_sum+lower_sum)
print(max(ans))