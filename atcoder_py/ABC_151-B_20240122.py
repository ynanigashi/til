num_of_tests, max_score, target_average = map(int, input().split())
scores = list(map(int, input().split()))
target_score = num_of_tests * target_average - sum(scores)
print(max(target_score, 0) if target_score <= max_score else -1)