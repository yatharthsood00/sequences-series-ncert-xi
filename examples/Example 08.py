'''Example 8: Insert 6 numbers between 3 and 24 such that the resulting sequence is
an A.P.'''

from fractions import Fraction

vals, nos = [3,24], 6
d = (vals[1] - vals[0])/(nos + 1)
[vals.insert(-1, (vals[0] + d*i)) for i in range(1, nos + 1)]
[print(Fraction(vals[i]).limit_denominator(100)) for i in range(len(vals))]
	