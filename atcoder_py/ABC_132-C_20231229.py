num_of_problems = int(input())
difficulties = list(map(int, input().split()))
sorted_difficulties = sorted(difficulties)
print(sorted_difficulties[num_of_problems//2] - sorted_difficulties[num_of_problems//2-1])