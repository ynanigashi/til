import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

x, y = map(int, input().split())
print(lcm(x, y))