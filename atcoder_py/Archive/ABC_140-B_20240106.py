num_of_foods = int(input())
eaten_orders = list(map(int, input().split()))
satisfactions = list(map(int, input().split()))
additional_satisfactions = list(map(int, input().split()))
satisfaction_sum = 0
for i in range(num_of_foods):
    satisfaction_sum += satisfactions[eaten_orders[i]-1]
    if i > 0 and eaten_orders[i] - eaten_orders[i-1] == 1:
        satisfaction_sum += additional_satisfactions[eaten_orders[i-1]-1]

print(satisfaction_sum)