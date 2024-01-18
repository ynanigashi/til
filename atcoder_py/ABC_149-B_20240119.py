takahashi_cookie, aoki_cookie, turn = map(int, input().split())
if takahashi_cookie <= turn:
    print(0, end=' ')
    print(max(aoki_cookie - (turn - takahashi_cookie),0))
else:
    print(takahashi_cookie - turn, end=' ')
    print(aoki_cookie)