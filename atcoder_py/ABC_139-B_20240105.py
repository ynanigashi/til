import math
num_of_sockets, target_num_of_sockets = map(int, input().split())
if target_num_of_sockets == 1:
    print(0)
else:
    print(math.ceil((target_num_of_sockets -1) / (num_of_sockets - 1)))
