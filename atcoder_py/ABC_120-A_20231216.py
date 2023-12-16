price, having_money, num_of_satisfied = map(int, input().split())
print(min(having_money // price, num_of_satisfied))