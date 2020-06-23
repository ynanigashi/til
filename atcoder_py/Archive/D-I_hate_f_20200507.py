#+の場合
i = 0
ans = 0
while ans <= 1000000000:
    i += 1
    ans = i**5 - (i-1)**5
print(i)#120

#-の場合
i = 0
ans = 0
while ans <= 1000000000:
    i -= 1
    ans = i**5 - (i-1)**5 
print(i)#-119

#2だった場合
i = 0
ans = 0
while ans <= 1000000000:
    i += 1
    ans = i**5 - (i-2)**5
print(i)#101