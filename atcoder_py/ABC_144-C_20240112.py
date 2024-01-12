n = int(input())
min_step = n - 1
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        min_step = min(min_step, i + n // i - 2)
        
print(min_step)
