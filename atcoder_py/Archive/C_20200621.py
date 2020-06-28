N = int(input())
ans = ""
while N > 26:
    N, mod = divmod(N, 26)
    if mod == 0: mod = 26 
    ans += chr(96+mod)
    if N < 27:break
ans += chr(96+mod) 
print(ans[::-1])