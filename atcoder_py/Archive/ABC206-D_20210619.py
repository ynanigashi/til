def is_palindrome(list):
    palindrome = True
    n = len(list)
    for i in range(n//2):
        if list[i] != list[n - i -1]:
            palindrome = False
            break
    return palindrome

n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n//2):
    f, l = a[i], a[n - i -1]
    if f == l: continue
    a = [l if i == f else i for i in a]
    cnt += 1
print(cnt)