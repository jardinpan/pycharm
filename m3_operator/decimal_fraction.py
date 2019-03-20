import decimal
import fractions

print(decimal.Decimal(0.1))
print(decimal.Decimal(1.1) + decimal.Decimal(2.2))
print(decimal.Decimal(1.1 + 2.2))
print(decimal.Decimal('1.1') + decimal.Decimal('2.2'))

print(fractions.Fraction(1.5))
print(fractions.Fraction(1, 3))
print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))

