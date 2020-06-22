N = int(input())
A_list = list(map(int, input().split()))
ans = 0
def get_div_num(n):
   arr = []
   for i in range(2, int(-(-n**0.5//1))+1):
       if n%i == 0:
           cnt=0
           while n%i == 0:
               cnt += 1
               n //= i
               arr.append(i**cnt)
   if n != 1:
       arr.append(n)
   return arr

for i, n in enumerate(A_list):
    not_div_flg = True
    for j in range(2, int(-(-n**0.5//1))+1):
       if n%j == 0:
           cnt=0
           while n%j == 0:
               cnt += 1
               n //= j
               if j**cnt in A_list[:i]+A_list[i+1:]:
                   not_div_flg = False
                   break
    if not_div_flg: break
    if n != 1 and n in A_list[:i]+A_list[i+1:]:break
    if not_div_flg: ans += 1
print(ans)
