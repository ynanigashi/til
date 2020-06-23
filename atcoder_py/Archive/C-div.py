def factorization(n):
    arr = []
    #nが素数だったときに追加するために
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
N = int(input())
ans = 0
if N != 1:
    fact_list = factorization(N)
    for _, i in fact_list:
        j = 1
        while i >= j:
            ans += 1
            i = i - j
            j += 1
            
print(ans)