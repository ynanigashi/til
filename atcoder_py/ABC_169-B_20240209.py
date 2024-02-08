max_num = 10**18
_ = int(input())
num_list = list(map(int, input().split()))
if 0 in num_list:
    print(0)
else:
    ans = 1
    for num in num_list:
        ans *= num
        if ans > max_num:
            print(-1)
            break
    else:
        print(ans)