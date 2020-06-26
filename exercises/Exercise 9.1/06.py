'''Q. Write the first five terms of each of the sequences in Exercises 1 to 6 whose nth
terms are: (((n^2)+5)/(4))*n'''

from fractions import Fraction
n = 5
terms = []
[terms.append(Fraction(i*(((i**2)+5)/4)).limit_denominator(100)) for i in range(1, n + 1)]
[print(terms[no]) for no in range(len(terms))]