div_num = 998244353
a, b, c, d, e, f = map(int, input().split())
print(((a*b*c)%div_num + div_num - (d*e*f)%div_num)%div_num)