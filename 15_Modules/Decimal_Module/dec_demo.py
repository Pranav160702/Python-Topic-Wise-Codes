import decimal 
from decimal import Decimal

d = Decimal(100)

print(d)

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))


print(Decimal('0.1') * Decimal('0.3'))

print(Decimal(1) / Decimal(8))

print(Decimal(1) / Decimal(3))
