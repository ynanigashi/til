n = int(input())
h = list(map(int, input().split()))
i = 0
answer = 0
while i < n - 1:
    j = i
    while j < n - 1 and h[j] >= h[j+1]:
        j += 1
    answer = max(answer, j - i)
    i = j if i != j else j + 1
print(answer)
