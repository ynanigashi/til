num_str = input()
cnt = 1
ans = 'No'
pre_char = '0'
for c in num_str:
    if c == pre_char:
        cnt += 1
    else:
        cnt = 1
        pre_char = c
    
    if cnt == 3:
        ans = 'Yes'
        break
 
print(ans)