'''How many terms of the A.P. – 6, -11/2, – 5, … are needed to give the sum –25?'''

from fractions import Fraction

vals, ssum, times, terms = [-6, ((-11)/2)], -25, 0, []
d = (vals[1] - vals[0])
while True:
	vals.append(vals[-1] + d)
	if sum(vals) == ssum:
		times = times + 1
		terms.append(len(vals))
		if times == 2:
			break
print("Terms needed =", end=" ")
for i in range(len(terms)):
	print(terms[i], end=" ")
	if i != len(terms) - 1:
		print("or", end=" ")