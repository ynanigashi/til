target_int, num_of_ints = map(int, input().split())
int_list = list(map(int, input().split()))

if num_of_ints == 0:
    print(target_int)
    exit()

for i in range(0, 100):
    if not target_int - i in int_list:
        print(target_int - i)
        break
    elif not target_int + i in int_list:
        print(target_int + i)
        break