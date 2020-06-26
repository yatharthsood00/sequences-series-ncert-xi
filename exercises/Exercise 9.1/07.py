'''Find the indicated terms in each of the sequences in Exercises 7 to 10 whose nth terms are: 4n – 3. 17th and 24th'''

from fractions import Fraction

t = [17, 24]
terms = []
[terms.append(4*i - 3) for i in t]
[print(terms[no]) for no in range(len(terms))]