'''14. Insert five numbers between 8 and 26 such that the resulting sequence is an A.P.'''

from fractions import Fraction

vals, nos = [8,26], 5
d = (vals[1] - vals[0])/(nos + 1)
[vals.insert(-1, (vals[0] + d*i)) for i in range(1, nos + 1)]
[print(Fraction(vals[i]).limit_denominator(100)) for i in range(1, len(vals) - 1)]
	