_ = input()
sec_of_problems = list(map(int, input().split()))
num_of_drinks = int(input())
total_sec = sum(sec_of_problems)

for _ in range(num_of_drinks):
    problem_no, solve_sec = map(int, input().split())
    problem_index = problem_no - 1
    print(total_sec - sec_of_problems[problem_index] + solve_sec)