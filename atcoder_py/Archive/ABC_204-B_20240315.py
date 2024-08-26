num_of_trees = int(input())
trees = list(map(int, input().split()))
answer = 0
for tree in trees:
    answer += max(0, tree - 10)

print(answer)