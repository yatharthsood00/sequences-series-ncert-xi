'''Find the 20th term of the G.P. 5/2, 5/4, 5/8...'''

from fractions import Fraction

vals, no = [5/2, 5/4, 5/8], 20
r = (vals[1]/vals[0])
print(r)
print(Fraction(vals[0]*(r**(no - 1))).limit_denominator(10000000))