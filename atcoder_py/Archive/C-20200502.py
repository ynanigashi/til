N, M, Q = map(int, input().split())
lists = [list(map(int, input().split())) for i in range(Q)]
ans = 0

def calc_score(A):
    score = 0
    for a, b, c, d in lists:
        if A[b - 1] - A[a - 1] == c:
            score += d
    return score

def dfs(A):
    global ans
    if len(A) == N:
        score = calc_score(A)
        ans = max(score, ans)
        return
    for n in range(A[-1], M + 1):
        dfs(A + [n])

dfs([1])
print(ans)