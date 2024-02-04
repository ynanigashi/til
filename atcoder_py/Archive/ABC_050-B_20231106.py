_ = input()
sec_of_problems = list(map(int, input().split()))
num_of_drinks = int(input())
total_sec = sum(sec_of_problems)

for _ in range(num_of_drinks):
    problem_no, solve_sec = map(int, input().split())
    problem_index = problem_no - 1
    print(total_sec - sec_of_problems[problem_index] + solve_sec)    

'''
for _ in range(num_of_drinks):
    problem_no, solve_sec = map(int, input().split())
    problem_index = problem_no - 1
    temp_list = [
        solve_sec if index == problem_index else value
        for index, value in enumerate(sec_of_problems)
    ]
    print(sum(temp_list))
'''