n = input()
for _ in range(len(n)+2):
    ans = "Yes" if n == n[::-1] else "No"
    if ans == "Yes": break
    n = "0"+n
print(ans)