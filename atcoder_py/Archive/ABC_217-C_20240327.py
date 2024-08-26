len_of_p = int(input())
p = list(map(int, input().split()))
q = [0] * len_of_p
for i in range(len_of_p):
    q[p[i]-1] = i + 1

print(*q, sep=' ')