'''Q. Write the first five terms of each of the sequences in Exercises 1 to 6 whose nth
terms are: (-1)^(n-1)*5^(n+1)'''

from fractions import Fraction
n = 5
terms = []
[terms.append(Fraction(((-1)**(i-1))*5**(i+1)).limit_denominator(100)) for i in range(1, n + 1)]
[print(terms[no]) for no in range(len(terms))]