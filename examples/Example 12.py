'''Find the sum of first 5 terms of the geometric
series: 1 + 2/3 + 4/9 + ...'''

from fractions import Fraction

vals, target = [1, 2/3], 5
r = vals[1]
[vals.append(vals[-1] * r) for i in range(2, target)]
print(f"Sum till {target} terms is = {Fraction(sum(vals)).limit_denominator(100)}")