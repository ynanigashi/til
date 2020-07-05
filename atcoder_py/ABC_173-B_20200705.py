N = int(input())
ans = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for _ in range(N):
    S = input()
    ans[S] += 1

for k, v in ans.items():
    print(k,'x',v)
