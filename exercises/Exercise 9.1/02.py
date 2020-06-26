'''Q. Write the first five terms of each of the sequences in Exercises 1 to 6 whose nth
terms are: n/(n + 1)'''

from fractions import Fraction
n = 5
terms = []
for i in range(1, n +1):
	terms.append(Fraction(round(i/(i+1), 10)).limit_denominator(10))
for t in range(len(terms)):
	print(terms[t])