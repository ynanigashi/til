#https://atcoder.jp/contests/abc166/submissions/12715523
n = int(input())
 
a = [i**5 for i in range(120)]
for i in range(120):
    for j in range(i+1,120):
        if a[j]-a[i] == n:
            print(j,i)
            break
        if a[j]+a[i] == n:
            print(j,-i)
            break
    else: continue
    break
