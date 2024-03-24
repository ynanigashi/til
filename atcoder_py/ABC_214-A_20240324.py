contest_number = int(input())
num_of_problems = 4
if contest_number >= 212:
    num_of_problems = 8
elif contest_number >= 126:
    num_of_problems = 6

print(num_of_problems)