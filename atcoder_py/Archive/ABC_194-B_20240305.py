num_of_employee = int(input())
employee = [list(map(int, input().split())) for _ in range(num_of_employee)]
min_a = min(list(map(lambda x: x[0], employee)))
min_a_index = list(map(lambda x: x[0], employee)).index(min_a) 
employee[min_a_index][1] += min_a
min_b = min(list(map(lambda x: x[1], employee)))

print(max(min_a, min_b))