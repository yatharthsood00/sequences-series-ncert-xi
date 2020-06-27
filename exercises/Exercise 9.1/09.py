'''Find the indicated terms in each of the sequences in Exercises 7 to 10 whose nth terms are: (-1)^(n-1)*n^3. 9th'''

from fractions import Fraction

t = [9]
terms = []
[terms.append((-1)**(i-1)*(i**3)) for i in t]
[print(Fraction(terms[no])) for no in range(len(terms))]