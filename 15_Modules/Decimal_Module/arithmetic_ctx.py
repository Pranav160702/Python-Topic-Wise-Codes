import decimal
from decimal import Decimal


ctx = decimal.getcontext()
ctx.prec = 10
ctx.rounding = decimal.ROUND_HALF_UP
print(decimal.getcontext())
