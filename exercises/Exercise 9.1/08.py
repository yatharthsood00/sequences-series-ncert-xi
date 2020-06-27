'''Find the indicated terms in each of the sequences in Exercises 7 to 10 whose nth terms are: (n^2)/(2^n). 7th'''

from fractions import Fraction

t = [7]
terms = []
[terms.append((i**2)/(2**i)) for i in t]
[print(Fraction(terms[no])) for no in range(len(terms))]