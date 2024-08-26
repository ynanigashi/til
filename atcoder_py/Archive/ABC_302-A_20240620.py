from decimal import Decimal, getcontext
from math import ceil

getcontext().prec = 100

a, b = map(Decimal, input().split())
print(ceil(a/b))