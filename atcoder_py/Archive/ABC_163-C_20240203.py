num_of_employees = int(input())
bosses = list(map(int, input().split()))
subordinates = [0] * num_of_employees
for boss in bosses:
    subordinates[boss-1] += 1
for subordinate in subordinates:
    print(subordinate)