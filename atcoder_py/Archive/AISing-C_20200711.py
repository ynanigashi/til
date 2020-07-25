import itertools
N = int(input())
rng = int(-(-N**0.5//1))
pat_list = list(itertools.product(range(1,rng),repeat=3))
cnt_list = [0 for i in range(rng**2*6)]
for X, Y, Z in pat_list:
    cnt_list[X**2+Y**2+Z**2+X*Y+Y*Z+Z*X] += 1

for i in range(1, N+1):
    print(cnt_list[i])