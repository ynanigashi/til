# def compute_factorial(n: int) -> int:
#     return 1 if n == 0 else n * compute_factorial(n - 1)
M = 1000000007
def compute_factorial_mod_1097(n: int) -> int:
    temp = 1
    for i in range(1, n+1):
        temp = temp*i % M
    
    return temp

n = int(input())

print(compute_factorial_mod_1097(n))
