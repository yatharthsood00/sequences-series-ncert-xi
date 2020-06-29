'''How many terms of the G.P. 3,3/2,3/4,... are needed to give the sum 3069/512?'''

from fractions import Fraction

vals, sums = [3, 3/2], 3069/512
r = vals[1]/vals[0]
while sum(vals) != sums:
	vals.append(vals[-1]*r)
print(f"No. of terms needed = {len(vals)}")