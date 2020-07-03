'''Find the 12th term of a G.P. whose 8th term is 192 and the common ratio is 2.'''

from fractions import Fraction
vals = []
tm1, r, pos, tgt = 192, 2, 8, 12
[vals.append(0) for i in range(0, pos - 1)]
vals.append(tm1)
for i in range(0, pos - 1):
	vals[i] = (vals[pos - 1] / r**(pos - 1))*(r**(i)) 
[vals.append(vals[-1]*r) for i in range(pos, 12)]
print(f"Required term: {vals[tgt - 1]}")