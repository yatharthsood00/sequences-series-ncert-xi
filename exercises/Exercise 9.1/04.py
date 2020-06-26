'''Q. Write the first five terms of each of the sequences in Exercises 1 to 6 whose nth
terms are: (2n - 3)/6'''

from fractions import Fraction
n = 5
terms = []
for i in range(1, n + 1):
	t = ((2*i - 3)/6)
	terms.append(Fraction(t).limit_denominator(100))
for no in range(len(terms)):
	print(terms[no])