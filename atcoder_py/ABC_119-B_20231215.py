num_of_otoshidama = int(input())
sum_of_otoshidama = 0.0
for _ in range(num_of_otoshidama):
    x, u = input().split()
    sum_of_otoshidama += float(x) if u == 'JPY' else 380000.0 * float(x)
print(sum_of_otoshidama)