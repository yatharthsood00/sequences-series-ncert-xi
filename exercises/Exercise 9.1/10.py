'''Find the indicated terms in each of the sequences in Exercises 7 to 10 whose nth terms are: (n*(n-2))/(n+3). 20th'''

from fractions import Fraction

t,terms = [20], []
[terms.append((i*(i-2))/(i+3)) for i in t]
[print(Fraction(terms[no]).limit_denominator(100)) for no in range(len(terms))]