sum_limit, product_limit = map(int, input().split())
count = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if (i + j + k <= sum_limit and 
                i * j * k <= product_limit):
                count += 1
print(count)  