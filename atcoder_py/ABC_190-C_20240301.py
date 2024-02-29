#公式回答を写経
import itertools
num_of_dishes, num_of_conditions = map(int, input().split())
conditions = [tuple(map(int, input().split())) for i in range(num_of_conditions)]
num_of_people = int(input())
choice = [tuple(map(int, input().split())) for i in range(num_of_people)]
answer = 0
# 全ての選択肢に対して、条件を満たすものを探す
for balls in itertools.product(*choice):
    balls = set(balls)
    count = sum(A in balls and B in balls for A, B in conditions)
    answer = max(answer, count)
print(answer)