_ = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
bob = 0

for i, j in enumerate(a):
    if i%2:
        bob += j
    else:
        alice += j

print(alice - bob)