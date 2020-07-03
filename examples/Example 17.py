'''Insert three numbers between 1 and 256 so that the resulting sequence
is a G.P.'''

from fractions import Fraction

vals, nos = [1, 256], 3
r = (vals[1]/vals[0])**(1/(nos + 1))
[vals.insert(-1, (vals[0]*(r*i))) for i in range(1, nos + 1)]
[print(Fraction(vals[i]).limit_denominator(100)) for i in range(len(vals))]
