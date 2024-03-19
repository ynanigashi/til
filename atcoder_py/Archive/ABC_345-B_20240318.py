from decimal import Decimal, getcontext
import math
getcontext().prec = 19
x = int(input())
print(math.ceil(x/Decimal(10)))