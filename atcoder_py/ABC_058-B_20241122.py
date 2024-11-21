odd_str = input()
even_str = input()
ans = ''
for i in range(len(odd_str)):
    ans += odd_str[i]
    if i < len(even_str):
        ans += even_str[i]

print(ans)