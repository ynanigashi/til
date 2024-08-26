num_of_people = int(input())
scores = list(map(int, input().split()))
scores_sorted = sorted(scores, reverse=True)
print(scores.index(scores_sorted[1]) + 1)