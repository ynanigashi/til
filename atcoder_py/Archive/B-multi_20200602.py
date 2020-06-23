input()
int_list = list(map(int, input().split()))
max_num = 10**18
ans = 1

if 0 in int_list:
    print(0)
    exit()
  
for i in int_list:
    ans *= i
    if ans > max_num:
        print(-1)
        break
else:
    print(ans)
