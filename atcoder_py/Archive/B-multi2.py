input()
int_list = list(map(int, input().split()))
max_num = 10**18
ans = 1
for i in int_list:
    ans *= i
    if ans > max_num:
        if min(int_list) == 0:
            print(0)
        else:
            print(-1)
        break
else:
    print(ans)
