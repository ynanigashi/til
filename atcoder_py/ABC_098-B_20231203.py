len_of_str, string = int(input()), input()
ans = 0
for i in range(1, len_of_str):
    ans = max(ans, len(set(string[:i]) & set(string[i:])))
print(ans)