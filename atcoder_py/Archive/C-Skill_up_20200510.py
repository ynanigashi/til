import itertools
N, M, X = map(int, input().split())
book_lists = [list(map(int, input().split())) for i in range(N)]
no_skill_flg = True
for i in range(1, N+1):
    for j in itertools.combinations(book_lists,i):
        sum_list = [0 for _ in range(M+1)]
        for book_date in j:
            for k, l in enumerate(book_date):
                sum_list[k] += l
        if all([s >= X for s in sum_list[1:]]):
            no_skill_flg = False
            if 'ans' in globals():
                ans = min(ans, sum_list[0])
            else:
                ans = sum_list[0]
print(ans if not no_skill_flg else -1)