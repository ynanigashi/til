n, q = map(int, input().split())
c = [0]
c += list(map(int,input().split()))
for _ in range(q):
    i,j = map(int, input().split())
    print(len(set(c[i:j+1])))